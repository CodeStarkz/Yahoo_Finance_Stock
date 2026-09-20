# Yahoo Finance Stock & Crypto Scraper

A web scraper designed to collect stock and cryptocurrency data from Yahoo Finance, orchestrated by Apache Airflow.

## Features

- **User-Agent Rotation:** Uses a middleware to rotate user agents for each request to avoid detection.
- **Proxy Support:** Uses a middleware to rotate through a predefined list of proxies for each request.
- **Airflow Orchestration:** Automates data ingestion, scraping, and database insertion workflows.

## Project Structure

```
/Users/abhisheksingh/Desktop/Yahoo_Finance_Stock/
├── YFS_Scraper/        # Scrapy project directory
│   ├── spiders/        # Spiders for scraping data
│   ├── middlewares.py  # Custom middleware (UA and Proxy rotation)
│   ├── pipelines.py    # Data processing pipeline
│   ├── settings.py     # Scrapy settings
│   ├── dags/           # Apache Airflow DAGs for orchestration
│   └── logs/           # Airflow execution logs
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

### Direct Scrapy Execution
To run the spider directly for testing, navigate to the `YFS_Scraper` directory and use the `scrapy` CLI:

```bash
cd YFS_Scraper
scrapy crawl YFS_spider
```

### Airflow Orchestration
The full data pipeline is managed by Airflow. Ensure Airflow is running, then trigger the DAG:

```bash
# Example command to trigger the ingestion DAG
airflow dags trigger YFS_ingestion_dag
```
Data will be processed and saved according to the pipeline configuration.
