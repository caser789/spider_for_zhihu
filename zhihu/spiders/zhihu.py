from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..settings import *

class ZhihuLoginSpider(CrawlSpider):
    name = 'zhihuspider1'
    allowed_domains = ['zhihu.com']
    start_urls = [r'http://www.zhihu.com']



    def __init__(self,*args, **kwargs):
        super(ZhihuLoginSpider,self).__init__(*args, **kwargs)
        self.headers =HEADERS
        self.cookies =COOKIES
        self.f = open('urls', 'wb')

    def start_requests(self):
        yield FormRequest(url='http://www.zhihu.com',  \
                              headers = self.headers, \
                              cookies =self.cookies,
                              callback = self.login)

    def login(self, response):
        for url in response.xpath(
                r'//div[@data-type="a"]//h3//@href').extract():
            yield Request(u'http://www.zhihu.com'+ url, callback=self.login)

    
'''
    def parse_item(self, response):
        print '*' * 30
        print response.url
'''
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
