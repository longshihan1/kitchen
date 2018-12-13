# -*- coding: utf-8 -*-
from urllib import parse

import scrapy
from scrapy import Request



class HaodouSpider(scrapy.Spider):
    name = 'haodou'
    allowed_domains = ['www.xiachufang.com']
    start_urls = ['http://www.xiachufang.com/category/51761/']

    def parse(self, response):
        #写法1
        lists = response.xpath("//div[@class='recipe recipe-215-horizontal pure-g image-link display-block']")
        for element in lists:
            detail_url=element.xpath("div/p[@class='name']/a/@href").extract()[0]
            yield Request(url=parse.urljoin(response.url, detail_url),callback=self.parse_detail)
        # 写法2
        #url_lists=response.xpath("//div/p[@class='name']/a/@href").extract()
        #for url in url_lists:
        #    print(url)
        text = response.xpath("//h1[@class='page-title']/text()").extract()[0]
        print(text)
        pass


    def parse_detail(self,response):
        title=response.xpath("//h1[@class='page-title']/text()").extract()[0]
        topimg=response.xpath("//div[@class='cover image expandable block-negative-margin']/img/@src").extract()[0]
        #/html/body/div[4]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/span[1]
        score=response.xpath("//div[@class='score float-left']/span[@class='number']/text()").extract()[0]
        cookcount = response.xpath("//div[@class='cooked float-left']/span[@class='number']/text()").extract()[0]
        author = response.xpath("//div[@class='author']/a/span/text()").extract()[0]
        author_img = response.xpath("//div[@class='author']/a/img/@src").extract()[0]
        one_message=response.xpath("//div[@class='desc mt30']/text()").extract()[0]
        tools_message=response.xpath("//div[@class='ings']/text()").extract()[0]
        message = response.xpath("//div[@class='steps']/text()").extract()[0]
        tip = response.xpath("//div[@class='tip']/text()").extract()[0]
        video_url=response.xpath("//iframe/@src").extract()[0]
        print(title)
        pass