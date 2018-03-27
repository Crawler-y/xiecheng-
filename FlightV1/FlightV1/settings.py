# -*- coding: utf-8 -*-

BOT_NAME = 'FlightV1'

SPIDER_MODULES = ['FlightV1.spiders']
NEWSPIDER_MODULE = 'FlightV1.spiders'
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 32
DOWNLOAD_FAIL_ON_DATALOSS = False
AUTOTHROTTLE_ENABLED = False
JOBDIR='D:\My Documents\Desktop\航班爬虫项目\FlightV1/fly_job1'
ITEM_PIPELINES = {
   'FlightV1.pipelines.Flightv1Pipeline': 300,
}
# DOWNLOADER_MIDDLEWARES = {
   # 'FlightV1.middlewares.Flightv1SpiderMiddleware': 543,
   # 'scrapy_crawlera.CrawleraMiddleware': 600
# }
# AUTOTHROTTLE_ENABLED = False
# DUPEFILTER_CLASS = 'scraper.duplicate_filter.CustomFilter'

#DOWNLOAD_TIMEOUT = 600
# LOG_FILE ='D:\My Documents\FlightV1\FlightV1/fl.log'
# LOG_LEVEL = 'INFO'


# DUPEFILTER_CLASS = 'scrapy.dupefilter.BaseDupeFilter'



# HTTPERROR_ALLOWED_CODES = [403]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'FlightV1 (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'Accept': 'application/json, text/javascript, */*; q=0.01',
#    'Accept-Encoding': 'gzip, deflate',
#    'Accept-Language': 'zh-CN,zh;q=0.9',
#    'Connection': 'keep-alive',
#    'dataType': "json",
#    'Content-Type': 'application/x-www-form-urlencoded',
   # 'Cookie': 'JSESSIONID=55FD148D1891F55F16BE3DDEB98ACD2A; X-LB=1.9.a.b2c89313; e60639e2b3f21fc7487c20700e6997a3=0d4a997a203beae98173a5ebb9aafb72; all=http%3A//www.umetrip.com/img/index/h_pic_3.jpg%2Chttp%3A//www.umetrip.com/img/index/h_pic_1.jpg%2Chttp%3A//www.umetrip.com/img/index/h_pic_2.jpg%2C0; isCheck=true0',
#    'Host': 'www.umetrip.com',
#    'Origin': 'http://www.umetrip.com',
#    'Referer': 'http://www.umetrip.com/mskyweb/page.do?p=ticket&dep=PEK&arr=PVG&date=2018-01-11',
#    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
#    'X-Requested-With': 'XMLHttpRequest'
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'FlightV1.middlewares.Flightv1SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOAD_TIMEOUT = 1
# IP_URL='https://proxy.mimvp.com/api/fetch.php?orderid=860170907095435229&num=1000&http_type=1'
# CRAWLERA_ENABLED = True
# CRAWLERA_USER = 'dcad29b0fa9c41829f813ddb226bc3ce'
#
# CRAWLERA_PASS = ''
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
