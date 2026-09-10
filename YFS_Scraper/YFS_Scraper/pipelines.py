# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import redis
from scrapy.exceptions import DropItem
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
            if value is not None:
                adapter[field] = str(value).strip()
            else:
                adapter[field] = None

        return item

class RedisDuplicatesPipeline:
    def __init__(self, redis_host, redis_port, redis_db):
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self.client = None

    @classmethod
    def from_crawler(cls, crawler):
        # Pull Redis settings from Scrapy's settings.py (with defaults)
        return cls(
            redis_host=crawler.settings.get('REDIS_HOST', 'localhost'),
            redis_port=crawler.settings.getint('REDIS_PORT', 6379),
            redis_db=crawler.settings.getint('REDIS_DB', 0),
        )

    def open_spider(self, spider):
        # Connect to Redis exactly once when the spider starts
        self.client = redis.Redis(
            host=self.redis_host,
            port=self.redis_port,
            db=self.redis_db
        )
        # Test connection gracefully
        try:
            self.client.ping()
            self.redis_available = True
            spider.logger.info("Successfully connected to Redis.")
        except redis.exceptions.ConnectionError:
            spider.logger.error("Could not connect to Redis, disabling duplicate filtering.")
            self.redis_available = False

    def close_spider(self, spider):
        # Safely close the Redis connection when done
        if self.client and self.redis_available:
            self.client.close()

    def process_item(self, item, spider):
        if not self.redis_available:
            return item

        adapter = ItemAdapter(item)
        # Try different fields for unique identification
        item_id = adapter.get('product_id') or adapter.get('symbol')

        if not item_id:
            # If no unique identifier is found, we might want to log this or just return the item
            spider.logger.warning(f"No unique identifier found for item: {item}")
            return item  # Skip if there is no ID to check

        # Redis SADD returns 1 if the item was added (new), and 0 if it already existed (duplicate)
        is_new = self.client.sadd('spider:seen_ids', item_id)

        if not is_new:
            raise DropItem(f"Duplicate item dropped by Redis: {item_id}")

        return item