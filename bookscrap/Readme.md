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

## 📊 Sample Output

```csv
Title,Price,Availability,Star_Rating
A Light in the Attic,51.77,In stock,3
Tipping the Velvet,53.74,In stock,1
Sharp Objects,47.82,In stock,4
```

## ✨ Features

- **Complete pagination** - Scrapes all pages automatically
- **Error handling** - Robust network and parsing error management
- **Respectful scraping** - 1-second delays between requests
- **Data cleaning** - Automatic price conversion and text standardization
- **Progress tracking** - Real-time scraping progress display

## 🛠️ Technical Details

- **Libraries**: requests, BeautifulSoup4, pandas
- **Target**: Static HTML website (no JavaScript rendering needed)
- **Output format**: CSV with clean, structured data
- **Legal**: Scrapes from practice website designed for learning

## 📝 License

Educational use - Practice project for learning web scraping techniques.
