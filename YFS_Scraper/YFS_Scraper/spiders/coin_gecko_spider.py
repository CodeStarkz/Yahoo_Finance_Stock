import scrapy
from ..items import  coingeckoscrapItem

class CoinGeckoSpiderSpider(scrapy.Spider):
    name = "coin_gecko_spider"
    custom_settings = {
        'FEEDS': {
            '/Users/abhisheksingh/Desktop/Yahoo_Finance_Stock/YFS_Scraper/scraped_output_storage_area/coin_gecko_Scraper_output_%(time)s.csv': {
                'format': 'csv',
                'encoding': 'utf-8',
                'overwrite': True,
            }
        }
    }
    allowed_domains = ["www.coingecko.com"]
    start_urls = ["https://www.coingecko.com/en/chains"]
    
    def __init__(self, *args, **kwargs):
        print("DEBUG: CoinGeckoSpiderSpider initializing...")
        super().__init__(*args, **kwargs)

    def parse(self, response):
        print("DEBUG: parse called")
        # Ensure we have the right content, debug
        with open("debug_page_parse.html", "w", encoding="utf-8") as f: f.write(response.text)
        rows = response.xpath('/html/body/div[2]/div/div/div[2]/main/div/div[4]/table/tbody/tr')

        for table_row in rows:
            item = coingeckoscrapItem()
            # Extract text using relative paths and .get()
            item['chains'] = table_row.xpath('.//td[2]//text()').get()
            item['trend_in_24hrs'] = table_row.xpath('.//td[4]//text()').get()
            item['trend_in_7_days'] = table_row.xpath('.//td[5]//text()').get()
            item['trend_in_30_days'] = table_row.xpath('.//td[6]//text()').get()
            item['volume_in_24_hrs'] = table_row.xpath('.//td[7]//text()').get()
            item['total_volume'] = table_row.xpath('.//td[8]//text()').get()
            item['dominance'] = table_row.xpath('.//td[9]//text()').get()
            item['rank'] = table_row.xpath('.//td[10]//text()').get()

            yield item

        next_page = response.xpath('//a[@aria-label="Next Page"]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse, meta={'selenium': True})
        else:
            self.logger.info('no next page')
