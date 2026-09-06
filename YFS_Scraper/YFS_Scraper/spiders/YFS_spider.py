import scrapy
from ..items import YfsScraperItem


class YfsSpiderSpider(scrapy.Spider):
    name = "YFS_spider"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/markets/crypto/all/?guccounter=1"]

    def parse(self, response):
        # locating data_container_table rows
        rows = response.xpath('//*[@id="main-content-wrapper"]/section[1]/div/div[3]/div/table/tbody/tr')
        for data_row in rows:
            item = YfsScraperItem()
            item['symbol'] = data_row.xpath('.//td[1]//span/text()').get()
            item['name'] = data_row.xpath('.//td[2]//text()').get()
            item['price'] = data_row.xpath('.//td[4]//span/text()').get()
            item['change'] = data_row.xpath('.//td[5]//span/text()').get()
            item['change_percent'] = data_row.xpath('.//td[6]//span/text()').get()
            item['market_cap'] = data_row.xpath('.//td[7]//span/text()').get()
            item['volume'] = data_row.xpath('.//td[8]//span/text()').get()
            item['volume_in_currency_24hrs'] = data_row.xpath('.//td[9]//span/text()').get()
            item['total_volume_in_all_currency_in_24_hours'] = data_row.xpath('.//td[10]//span/text()').get()
            item['circulating_supply'] = data_row.xpath('.//td[11]//span/text()').get()
            item['week_52_change'] = data_row.xpath('.//td[12]//span/text()').get()
            yield item

        # next page locator
        next_page = response.xpath('//*[@id="main-content-wrapper"]/section[1]/div/div[4]/div[3]/button[2]').get()
        if next_page:
            yield response.follow(next_page, self.parse)
        else:
            print('no next page')

