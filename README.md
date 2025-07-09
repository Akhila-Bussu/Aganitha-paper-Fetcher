# Aganitha Paper Fetcher (PubMed API CLI Tool)

This project is a command-line tool that fetches research papers from PubMed based on a user query and filters papers with at least one non-academic (pharma/biotech) author.

---
## 📦 Features
- Fetches PubMed articles using PubMed’s E-Utilities API
- Identifies non-academic authors based on affiliations (e.g., containing words like *pharma*, *biotech*, *Inc*, etc.)
- Exports results as CSV
- Supports command-line options: `--debug`, `--file`, `--help`

---
## 🚀 Installation

```bash
poetry install
Usage
bash
Copy
Edit
poetry run get-papers-list "cancer AND 2024[PDAT]" --file output.csv --debug

📁 Output Format
PubmedID	Title	Publication Date	Non-academic Author(s)	Company Affiliation(s)	Corresponding Author Email

🔧 Tools Used
Python 3.10+
Poetry
httpx
Git & GitHub
LLM assistance via OpenAI (ChatGPT)

💡 Notes
You can modify fetcher.py to improve filtering.
Company affiliations are detected based on keywords (pharma, biotech, inc, corp, ltd, llc, etc.)
Emails are parsed from affiliation strings (if available).

👤 Author
Akhila Bussu

yaml
Copy
Edit

---

Then click **“Commit changes”** ✅

---

Would you like to move on next to:

✅ Uploading the `cli.py` file (command-line interface)?  
✅ Or generate the `pyproject.toml` file for Poetry setup?

Let me know what you want help with next.






You said:
in readme file i need t
