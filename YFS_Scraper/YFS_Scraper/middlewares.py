# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# ... (other classes remain unchanged until UserAgentMiddleWare)

class UserAgentMiddleWare:
    def __init__(self):
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
        ]
    
    def process_request(self, request, spider):
        request.headers.setdefault("User-Agent", random.choice(self.user_agent_list))
        return None

class ProxyMiddleWare:
    def __init__(self):
        self.proxy_list = ["172.16.31.10:8080", "172.16.58.3:8080", "172.16.31.10:8080", "172.16.58.3:8080"]
        
    def process_request(self, request, spider):
        request.meta["proxy"] = random.choice(self.proxy_list)
        return None