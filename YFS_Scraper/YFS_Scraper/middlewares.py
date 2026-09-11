# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class UserAgentMiddleWare:
    def __init__(self):
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        ]
    
    def process_request(self, request, spider):
        request.headers.setdefault("User-Agent", random.choice(self.user_agent_list))
        request.headers.setdefault("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
        request.headers.setdefault("Accept-Language", "en-US,en;q=0.5")
        request.headers.setdefault("Accept-Encoding", "gzip, deflate, br")
        request.headers.setdefault("Referer", "https://www.google.com/")
        return None

class ProxyMiddleWare:
    def __init__(self):
        self.proxy_list = ["172.16.31.10:8080", "172.16.58.3:8080", "172.16.31.10:8080", "172.16.58.3:8080"]
        
    def process_request(self, request, spider):
        request.meta["proxy"] = random.choice(self.proxy_list)
        return None

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.http import HtmlResponse
import time

class SeleniumMiddleware:
    def __init__(self):
        print("DEBUG: SeleniumMiddleware initializing...")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("DEBUG: SeleniumMiddleware initialized.")

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_request(self, request, spider):
        print(f"DEBUG: process_request called for {request.url}, meta: {request.meta}")
        # Always use selenium for now to test
        self.driver.get(request.url)
        time.sleep(5) # Increase sleep to ensure rendering
        with open("debug_page.html", "w", encoding="utf-8") as f: f.write(self.driver.page_source)
        print(f"DEBUG: Saved debug_page.html in {os.getcwd()}")
        return HtmlResponse(request.url, body=self.driver.page_source, encoding='utf-8', request=request)

    def spider_closed(self, spider):
        self.driver.quit()
