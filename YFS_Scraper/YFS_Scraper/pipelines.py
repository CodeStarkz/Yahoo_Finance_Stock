# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter

class YfsScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)


        fields = [
            'price', 'change', 'change_percent', 
            'market_cap', 'volume', 'volume_in_currency_24hrs', 
            'total_volume_in_all_currency_in_24_hours', 
            'circulating_supply', 'week_52_change','symbol', 'name'
        ]

        # Process string fields
        for field in fields:
            value = adapter.get(field)
            adapter[field] = str(value).strip() if value else None



        return item
