import argparse
import csv
import logging
from fetcher import search_pubmed, fetch_details

def save_to_csv(data, filename):
    if not data:
        print("No matching papers found.")
        return

    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} records to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fetch non-academic PubMed papers based on query")
    parser.add_argument("query", type=str, help="PubMed query")
    parser.add_argument("-f", "--file", type=str, help="Save output to CSV file")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    ids = search_pubmed(args.query, debug=args.debug)
    papers = fetch_details(ids, debug=args.debug)

    if args.file:
        save_to_csv(papers, args.file)
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
