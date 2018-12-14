# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KitchenItem(scrapy.Item):
    title = scrapy.Field()  # Field()能够接收和传递任何类型的值,类似于字典的形式
    create_date = scrapy.Field()  # 创建时间
    topimg=scrapy.Field()#头图
    url = scrapy.Field()  # 文章路径
    object_id = scrapy.Field()  # 文章内容的md5的哈希值，能够将长度不定的 url 转换成定长的序列
    score = scrapy.Field()
    cookcount = scrapy.Field()
    author = scrapy.Field()
    author_img = scrapy.Field()
    desmessage = scrapy.Field()
    imgsmessage = scrapy.Field()
    stepsmessage = scrapy.Field()
    tip = scrapy.Field()
    videourl = scrapy.Field()
