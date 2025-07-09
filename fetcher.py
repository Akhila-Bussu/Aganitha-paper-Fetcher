import httpx
from typing import List, Dict
from xml.etree import ElementTree as ET
import logging

BASE_ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
BASE_EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def search_pubmed(query: str, retmax: int = 50, debug: bool = False) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": retmax
    }
    response = httpx.get(BASE_ESEARCH_URL, params=params)
    response.raise_for_status()
    ids = response.json()["esearchresult"].get("idlist", [])
    if debug:
        logging.debug(f"Found {len(ids)} papers for query '{query}'")
    return ids

def fetch_details(pubmed_ids: List[str], debug: bool = False) -> List[Dict]:
    ids_str = ",".join(pubmed_ids)
    params = {
        "db": "pubmed",
        "id": ids_str,
        "retmode": "xml"
    }
    response = httpx.get(BASE_EFETCH_URL, params=params)
    response.raise_for_status()
    root = ET.fromstring(response.content)

    results = []
    for article in root.findall(".//PubmedArticle"):
        try:
            pmid = article.findtext(".//PMID")
            title = article.findtext(".//ArticleTitle")
            pub_date = article.findtext(".//PubDate/Year") or "Unknown"
            authors_info = []
            companies = []
            emails = []
            for author in article.findall(".//Author"):
                affiliation = author.findtext(".//Affiliation") or ""
                name = f"{author.findtext('ForeName') or ''} {author.findtext('LastName') or ''}".strip()
                if any(word in affiliation.lower() for word in ["pharma", "biotech", "inc", "ltd", "corp", "llc"]):
                    authors_info.append(name)
                    companies.append(affiliation)
                if "@" in affiliation:
                    emails.append(affiliation.split()[-1])

            if authors_info:
                results.append({
                    "PubmedID": pmid,
                    "Title": title,
                    "Publication Date": pub_date,
                    "Non-academic Author(s)": "; ".join(authors_info),
                    "Company Affiliation(s)": "; ".join(set(companies)),
                    "Corresponding Author Email": "; ".join(set(emails))
                })
        except Exception as e:
            if debug:
                logging.warning(f"Failed to parse article: {e}")
    return results
