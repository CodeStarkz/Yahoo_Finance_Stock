import scrapy
from ..items import  coingeckoscrapItem

class CoinGeckoSpiderSpider(scrapy.Spider):
    name = "coin_gecko_spider"
    allowed_domains = ["www.coingecko.com"]
    start_urls = ["https://www.coingecko.com/en/chains"]

    def parse(self, response):
        whole_data_box=response.xpath('//table[@class="tw-border-y tw-border-gray-200 dark:tw-border-moon-700 tw-divide-y tw-divide-gray-200 dark:tw-divide-moon-700 [&>tbody:first-of-type]:!tw-border-t-0 tw-w-full sortable"]').getall()
        table_body=whole_data_box.xpath('//tbody[@class="tw-divide-y tw-divide-gray-200 tw-min-w-full dark:tw-divide-moon-700"]')
        for table_row in table_body:
            item=coingeckoscrapItem()
            item['chains']=table_row.xpath('//div[@class="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5"]/text()')
            item['trend_in_24hrs']=table_row.xpath('//td[@data-sort="0"]//i/text()')
            item['trend_in_7_days']=table_row.xpath('')

        pass
