# Yahoo Finance Stock Scraper

A Scrapy-based web scraper designed to collect stock data from Yahoo Finance(Cryptos).

## Features

- **User-Agent Rotation:** Uses a middleware to rotate user agents for each request to avoid detection.
- **Proxy Support:** Uses a middleware to rotate through a predefined list of proxies for each request.

## Project Structure

```
/Users/abhisheksingh/Desktop/Yahoo_Finance_Stock/
├── YFS_Scraper/        # Scrapy project directory
│   ├── spiders/        # Spiders for scraping data
│   ├── middlewares.py  # Custom middleware (UA and Proxy rotation)
│   ├── pipelines.py    # Data processing pipeline
│   ├── settings.py     # Scrapy settings
└── ...
```

## Setup

This project uses `uv` for dependency management.

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

## Usage

To run the spider, navigate to the `YFS_Scraper` directory and use the `scrapy` CLI:

```bash
cd YFS_Scraper
scrapy crawl YFS_spider
```

Data will be saved to `output.csv` (or as configured in the project settings).
