# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter
from .items import YfsScraperItem, fobesItem

class UnifiedScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        spider_name = spider.name
        
        if isinstance(item, YfsScraperItem):
            fields = [
                'price', 'change', 'change_percent', 
                'market_cap', 'volume', 'volume_in_currency_24hrs', 
                'total_volume_in_all_currency_in_24_hours', 
                'circulating_supply', 'week_52_change','symbol', 'name'
            ]
        elif isinstance(item, fobesItem):
            fields = [
                'name', 'price', 'in_last_1_hour', 'in_last_24_hours', 
                'in_last_7_days', 'Market_cap', 'volume_24h'
            ]
        else:
            return item

        # Process string fields
        for field in fields:
            value = adapter.get(field)
            if value is not None:
                adapter[field] = str(value).strip()
            else:
                adapter[field] = None

        return item
