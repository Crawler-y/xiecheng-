# -*- coding: utf-8 -*-
import scrapy
import random
import requests
import time
import json
from scrapy import Request
from FlightV1.items import Flightv1Item
import os


class FlySpider(scrapy.Spider):
    name = 'fly'
    allowed_domains = ['ctrip.com']
    # start_urls = ['http://ctrip.com/']

    def __init__(self):
        headr = [
                 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                 "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                 "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                 "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                 "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                 "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                 "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {
             "Host": "flights.ctrip.com",
             "User-Agent": random.choice(headr),
             "Referer": "://flights.ctrip.com/booking/SHA-BJS-day-1.html?DDate1=2018-01-07",
             "Connection": "keep-alive",
             'X-Crawlera-Cookies': 'disable'
         }
    def start_requests(self):
    # j=u'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=BJS&ACity1=CGQ&SearchType=S&DDate1=2018-03-11&IsNearAirportRecommond=0&LogToken=d5c2cdde121640c587b2737a160555cc&rk=6.87741369292242094159&CK=B4828167808BE5DE87C5814B02C113A3&r=0.44130167627926424060312'
        os.chdir('D:\My Documents\Desktop\航班爬虫项目\FlightV1\FlightV1\spiders')
        with open('need_url',encoding='utf-8')as f:
            urls = eval(f.read())
            k = [url.replace('日期','2018-02-28')for url in urls]
            for i in k:
                yield Request(i, headers=self.headers, )

    def parse(self,response):
        time.sleep(1)
        try:
            jsonData = json.loads(response.text, encoding='utf-8')
            if jsonData['fis'] is not None:
                # print(jsonData)
                for dat in jsonData['fis']:
                    item=Flightv1Item()
                    item['fly'] = 'xiecheng'
                    item['start_site'] = dat['dpbn']
                    item['end_site'] = dat['apbn']
                    item['start_time'] = dat['dt']  # , '%Y-%m-%d %H:%M:%S'
                    item['end_time'] = dat['at']  # , '%Y-%m-%d %H:%M:%S')
                    item['fly_type'] = dat['fn']
                    item['money'] = dat['lp']
                    item['start'] = dat['dcn']
                    item['end'] = dat['acn']
                    tmp=eval(dat['confort'])
                    item['punctuality']=tmp['HistoryPunctualityArr']
                    yield item
        except Exception as e:
            print(e)

