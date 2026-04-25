# ⚖️ Court Data Fetcher — Indian District Court Case Scraper

A Flask web application that lets users search and retrieve Indian court case details in real time from the eCourts public portal using Playwright-based scraping.

> ✅ Built as part of an internship task. Focused on real-world scraping, structured data extraction, and robust error handling.

---

## What It Does

- Searches court cases by Case Type, Case Number, and Filing Year
- Scrapes real-time case data from the eCourts public website
- Extracts parties involved, filing dates, next hearing dates, and latest order PDF links
- Presents results in a clean Bootstrap-styled dashboard
- Provides downloadable PDF links for the latest court orders

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Flask (Python) |
| Scraping | Playwright |
| Frontend | HTML, Bootstrap |
| Target Site | eCourts India (Faridabad District Court) |

---

## Project Structure

```
Court-data-fetcher/
├── app/               # Flask application and scraping logic
├── run.py             # Application entry point
├── requirements.txt
└── README.md
```

---

## Setup & Run

```bash
git clone https://github.com/Siddhimudgal1417/Court-data-fetcher.git
cd Court-data-fetcher

pip install -r requirements.txt
playwright install chromium

python run.py
```

Open [http://localhost:5000](http://localhost:5000) to access the dashboard.

---

## Key Features

- 🔎 Search by case type, number, and filing year
- ⚡ Real-time scraping from live eCourts portal
- 📄 Direct PDF link for latest court order/judgment
- 🧾 Clear display of case metadata and party information
- 🎨 Bootstrap-styled clean dashboard UI

---

## Target Court

Faridabad District Court, Haryana — via [https://districts.ecourts.gov.in/faridabad](https://districts.ecourts.gov.in/faridabad)

---

## Skills Demonstrated

`Python` `Flask` `Playwright` `Web Scraping` `HTML Parsing` `Bootstrap` `Error Handling`

---

**Author:** Siddhi Mudgal · [LinkedIn](https://linkedin.com/in/https://www.linkedin.com/in/siddhi-mudgal/) · [GitHub](https://github.com/Siddhimudgal1417)
