# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY= 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False
COOKIES = {
       '_za':r'e7e080c8-0496-497a-81e5-a632fe69f8e0',
       '_ga':r'GA1.2.1831688535.1433559255', 
       '_xsrf':r'cce379f8a0994762597517c0dc62014f', 
       'q_c1':r'01c8ec1ec0e54ed0a1a00f7c5d13b6ac|1438906673000|1433559275000', 
       'cap_id':r"M2IwM2NiNmUyYzI1NGU0YWI2ZWI3YmVkOGYzM2M5ZDA=|1439005642|84b572264ba88071c76b7995fb4d6c35d82650ec", 
       'tc':r'AQAAAFTaN2eBogwAEBxvpu/ot06I689a',
       '__utma':r'51854390.1831688535.1433559255.1439789178.1439789178.1', 
       '__utmc':r'51854390', 
       '__utmz':r'51854390.1439789178.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)', 
       '__utmv':r'51854390.100-1|2=registration_date=20131211=1^3=entry_date=20131211=1',
       'z_c0':r"QUFEQU15NGlBQUFYQUFBQVlRSlZUZEViLVZYZU1reHl3a0JoYy1RbFlQTXpaWThjVUdqTnNnPT0=|1439796945|3208d2be014f03d3fb7b1cdb950bc62b6160b752", 
       'unlock_ticket':r"QUFEQU15NGlBQUFYQUFBQVlRSlZUZG1WMFZVWG82UGJGU00xQm5QYmZvQlVoN2pURmM1OHRRPT0=|1439796945|5d5e9dc7a09b95ae134cdd1e481318f42787f5c5", 
        }

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
HEADERS = {
        "Host": "www.zhihu.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
        "Referer": "http://www.zhihu.com/",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Upgrade-Insecure-Requests": "1",
        }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihu.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
