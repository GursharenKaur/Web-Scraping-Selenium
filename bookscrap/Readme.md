# 📚 Books to Scrape - Web Scraper

A Python web scraper that extracts book data from [Books to Scrape](https://books.toscrape.com/) - a safe practice website for web scraping.

## 🎯 What it does

Scrapes **ALL books** from the website and extracts:
- **Title** - Book name
- **Price** - Numeric price value
- **Availability** - In stock / Out of stock
- **Star Rating** - 1-5 star rating

## 🚀 Quick Start

### Prerequisites
```bash
pip install requests beautifulsoup4 pandas
```

### Run the scraper
```bash
python book_scraper.py
```

### Output
- **CSV file**: `books.csv` with all book data (1000+ books)
- **Console stats**: Summary statistics and progress tracking


