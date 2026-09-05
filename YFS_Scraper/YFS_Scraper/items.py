# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YfsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Defining item to scrape
    symbol=scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
    change=scrapy.Field()
    change_percent=scrapy.Field()
    market_cap=scrapy.Field()
    volume=scrapy.Field()
    volume_in_currency_24hrs=scrapy.Field()
    total_volume_in_all_currency_in_24_hours=scrapy.Field()
    circulating_supply=scrapy.Field()
    week_52_change=scrapy.Field()
    pass
