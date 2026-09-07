import scrapy


class CoinGeckoSpiderSpider(scrapy.Spider):
    name = "coin_gecko_spider"
    allowed_domains = ["www.coingecko.com"]
    start_urls = ["https://www.coingecko.com/en/chains"]

    def parse(self, response):
        pass
