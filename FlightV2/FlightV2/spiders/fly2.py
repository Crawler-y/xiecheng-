# -*- coding: utf-8 -*-
import scrapy
import random
import requests
import time
import json
from scrapy import Request
from FlightV2.items import Flightv2Item


class FlySpider(scrapy.Spider):
    name = 'fly2'
    allowed_domains = ['umetrip.com']
    start_urls = ['www.umetrip.com']

    def start_requests(self):
        headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Content-Length':'34',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'JSESSIONID=C16C5607BE169FAB2C23A5E6DF1F7524; e60639e2b3f21fc7487c20700e6997a3=ab8dfc55479ed11f10bf8c78f13eca32; all=http%3A//www.umetrip.com/img/index/h_pic_1.jpg%2Chttp%3A//www.umetrip.com/img/index/h_pic_2.jpg%2Chttp%3A//www.umetrip.com/img/index/h_pic_3.jpg%2C0; isCheck=true0; X-LB=1.8.9.443301ed',
        'Host':'www.umetrip.com',
        'Origin:http':'//www.umetrip.com',
        'Referer':'http://www.umetrip.com/mskyweb/page.do?p=ticket&dep=NAY&arr=SHA&date=2018-01-11&channel=',
        'X-Requested-With':'XMLHttpRequest',
        "User-Agent": "Mozilla/5.0WindowsNT6.2;WOW64)AppleWebKit/535.24KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
         }
        with open('D:\My Documents\Desktop\航班爬虫项目\FlightV2\FlightV2\spiders\dd.text')as f:
            stie = f.read().split(',')
        for i in range(1,32):
            for j in stie:
                for k in stie:
                    data={
                    'dep':j,
                    'arr':k,
                    'begDate':'2018-02-25'#+str(i)
                    }
                    url='http://www.umetrip.com/mskyweb/tk/dm.do'
                    yield scrapy.FormRequest(url,callback=self.parse_page ,formdata=data,)#headers=headers, )
    def parse_page(self,response):
        try:
            rsp=json.loads(response.text)
            if rsp['parray'] is not None:
                for datas in rsp['parray']:
                    item=Flightv2Item()
                    item['fly']='hanglv'
                    item['start_site']=datas["pbegairport"]
                    item['end_site']=datas["pendairport"]
                    item['start_time']=datas["pbegtime"]
                    item['end_time']=datas["pendtime"]
                    item['fly_type'] = datas["pflynum"]
                    item['money'] = datas["pprice"]
                    item['end'] = datas["pendcity"]
                    item['start'] = datas["pbegcity"]
                    item['punctuality']=datas["ontimeperformance"]+'%'
                    print(item)
                    yield item
        except Exception as e:
            print('该航班{}不存在'.format(e))
