# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Flightv2Item(scrapy.Item):
    fly=scrapy.Field()
    price=scrapy.Field()
    start_time=scrapy.Field()
    end_time = scrapy.Field()
    start_site=scrapy.Field()
    end_site = scrapy.Field()
    fly_type=scrapy.Field()
    money=scrapy.Field()
    start=scrapy.Field()
    end=scrapy.Field()
    punctuality=scrapy.Field()
