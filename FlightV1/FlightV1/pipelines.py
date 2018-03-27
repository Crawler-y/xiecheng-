# -*- coding: utf-8 -*-

import json

class Flightv1Pipeline(object):

    def process_item(self, item, spider):
        if item['fly'] =='xiecheng':
            with open("D:\My Documents\Desktop\航班爬虫项目/携程数据.json", "a")as f:
                js_dt = json.dumps(dict(item), ensure_ascii=False) + ",\n"
                f.write(js_dt)
                return item
        elif item['fly'] == 'hanglv':
            with open("D:\My Documents\Desktop\航班爬虫项目/航旅数据.json", "a")as f2:
                js_dt2 = json.dumps(dict(item), ensure_ascii=False) + ",\n"
                f2.write(js_dt2)
                return item

