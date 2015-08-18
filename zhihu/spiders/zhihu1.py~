from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..settings import *

class ZhihuLoginSpider(CrawlSpider):
    name = 'zhihuspider2'
    allowed_domains = ['zhihu.com']
    start_urls = [r'http://www.zhihu.com']
    
    rules = (
        Rule(LinkExtractor(allow=('.*?(/about)$',)),
            callback='parse_about', follow=True),
        Rule(LinkExtractor(allow=('.*?(/followers)$',)),
            callback='parse_followers', follow=True),
        Rule(LinkExtractor(allow=('.*?(/followees)$',)),
            callback='parse_followees', follow=True),
        Rule(LinkExtractor(allow=('^(/people/)([A-Za-z0-9-]*)$',)),
            callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=('/people/\d+')), 
            callback='parse_item', follow=True),
        )


    def __init__(self,*args, **kwargs):
        super(ZhihuLoginSpider,self).__init__(*args, **kwargs)
        self.headers =HEADERS
        self.cookies =COOKIES
        self.f = open('urls', 'wb')

    def start_requests(self):
        yield FormRequest(url='http://www.zhihu.com',  \
                              headers = self.headers, \
                              cookies =self.cookies)
    def parse_item(self, response):
        print '*' * 30
        print response.url
    def parse_about(self, response):
        print "#" * 40
        print response.url
    def parse_followers(self, response):
        print '-' * 35
        print response.url
    def parse_followees(self, response):
        print '+' * 45
        print response.url
'''
    rules = (
        Rule(LinkExtractor(allow=(r'^(/people/)[A-Za-z0-9-]*(/about)$',)),
            callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=(r'^(/people/)[A-Za-z0-9-]*(/followers)$',)),
            callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=(r'^(/people/)[A-Za-z0-9-]*(/followees)$',)),
            callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=(r'^(/people/)([A-Za-z0-9-]*)$',)),
            callback='parse_item', follow=True))
'''

