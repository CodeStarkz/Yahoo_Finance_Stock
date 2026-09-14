import scrapy
import json
from .. items import fobesItem


class FobesSpider(scrapy.Spider):
    name = "fobes"
    custom_settings = {
        'FEEDS': {
            '/Users/abhisheksingh/Desktop/Yahoo_Finance_Stock/YFS_Scraper/scraped_output_storage_area/fobes_Scraper_output_%(time)s.csv': {
                'format': 'csv',
                'encoding': 'utf-8',
                'overwrite': True,
            }
        }
    }
    allowed_domains = ["www.forbes.com"]
    start_urls = ["https://www.forbes.com/digital-assets/crypto-prices/"]

    def parse(self, response):
        rows=response.xpath('.//tbody[@role="rowgroup"]/tr')
        for row in rows:

            item = fobesItem()
            item["name"]=row.xpath('.//td[2]//span[@class="Table_tableCellName__hYTfr"]/text()').get()
            item["price"]=row.xpath('.//td[3]//text()').get()
            item['in_last_1_hour']=row.xpath('.//td[4]//text()').get()
            item['in_last_24_hours']=row.xpath('.//td[5]//text()').get()
            item['in_last_7_days']=row.xpath('.//td[6]//text()').get()
            item['Market_cap']=row.xpath('.//td[7]//text()').get()
            item['volume_24h']=row.xpath('.//td[8]//text()').get()

            yield item

        next_data_script = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        if next_data_script:
            data = json.loads(next_data_script)
            build_id = data['buildId']
            
            for page in range(2, 5):
                end_point_url = f"https://www.forbes.com/digital-assets/_next/data/{build_id}/crypto-prices.json?page={page}"
                yield scrapy.Request(url=end_point_url, callback=self.parse_json)

    def parse_json(self, response):
        data = response.json()
        assets = data['pageProps']['initialData']['cryptoPricesServerData']['assets']
        for asset in assets:
            item = fobesItem()
            item["name"] = asset.get("name")
            item["price"] = asset.get("price")
            item['in_last_1_hour'] = asset.get("percentage_1h")
            item['in_last_24_hours'] = asset.get("percentage")
            item['in_last_7_days'] = asset.get("percentage_7d")
            item['Market_cap'] = asset.get("marketCap")
            item['volume_24h'] = asset.get("volume")
            yield item





