# Yahoo Finance Stock & Crypto Scraper

This project is a sophisticated web scraping and data orchestration framework designed to collect real-time data from financial and cryptocurrency platforms. The current architecture focuses on reliable data ingestion, with a future roadmap aimed at building autonomous trading capabilities powered by Large Language Models (LLMs).

## Current Architecture

### Core Components
- **Scrapy Framework:** Used for high-performance web crawling.
- **Data Sources:** 
  - Yahoo Finance (Stocks/Financials)
  - Forbes (Market Insights)
  - CoinGecko (Cryptocurrency Data)
- **Data Orchestration:** Managed by **Apache Airflow**, ensuring automated, scheduled data collection pipelines.
- **Infrastructure:**
  - **Proxy/User-Agent Rotation:** Middleware implemented to maintain anonymity and avoid rate-limiting.
  - **Storage:** Data is ingested into intermediate and processed storage areas in CSV format for analysis.
  - **Environment Management:** Managed via `uv` for consistent dependency handling.

## Project Structure

```text
/Users/abhisheksingh/Desktop/Yahoo_Finance_Stock/
├── YFS_Scraper/              # Main Scrapy project directory
│   ├── spiders/              # Individual scrapers
│   │   ├── YFS_spider.py     # Yahoo Finance data collector
│   │   ├── fobes.py          # Forbes data collector
│   │   └── coin_gecko_spider.py # CoinGecko data collector
│   ├── middlewares.py        # Anonymization & rotation logic
│   ├── pipelines.py          # Data cleaning and storage pipeline
│   ├── settings.py           # Scrapy configuration
│   └── Airflow/              # Airflow orchestration
│       └── dags/             # Workflow definitions
├── main.py                   # Central entry point for future automation
└── scraped_output_storage_area/ # Processed data output
```

## Setup and Installation

This project utilizes `uv` to manage the Python environment.

1. **Clone the repository** and navigate to the root directory.
2. **Install dependencies:**
   ```bash
   uv sync
   ```
3. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

## Running the Scrapers

To perform manual data collection or test specific spiders, navigate to the `YFS_Scraper` directory:

```bash
cd YFS_Scraper
scrapy crawl [spider_name]
```
*(Available spiders: `YFS_spider`, `fobes`, `coin_gecko_spider`)*

## Future Roadmap: Autonomous Trading & AI Analysis

The project is evolving from a data collection tool into an autonomous trading system. The roadmap is divided into three key phases:

### 1. Advanced Data Analysis
Implement robust data processing pipelines to convert raw CSV output into structured time-series data suitable for technical analysis.

### 2. LLM-Powered Insight Generation
Integrate Large Language Models to:
- **Sentiment Analysis:** Analyze market news (from sources like Forbes) to gauge market sentiment.
- **Trend Interpretation:** Use LLMs to interpret complex technical indicators alongside qualitative news data.
- **Decision Support:** Develop AI agents that provide buy/sell recommendations based on synthesized quantitative and qualitative data.

### 3. Automated Trading Execution
Develop secure modules to interact with crypto/NFT exchange APIs to:
- Place buy/sell orders based on AI-driven decisions.
- Implement risk management and portfolio rebalancing logic.
- Monitor order execution and account performance in real-time.

---
*This project is designed for educational and research purposes. Always exercise caution when implementing automated trading systems.*
