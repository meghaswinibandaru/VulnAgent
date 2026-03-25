#  Vulnerability Grouping Agent

##  Description
This project processes vulnerability data from Excel files and groups them based on:
- Server Name
- Class
- Shared Vulnerability Solutions

##  Features
- Upload Excel file
- Filter by IP ranges
- Group vulnerabilities
- Generate output Excel
- Download results

##  Tech Stack
- FastAPI
- Pandas
- OpenPyXL
- HTML, CSS

##  How to Run

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload