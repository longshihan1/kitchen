# -*- coding: utf-8 -*-
from urllib import parse

import scrapy
from scrapy import Request

from kitchen.items import KitchenItem
from kitchen.utils.common import gen_md5


class HaodouSpider(scrapy.Spider):
    name = 'haodou'
    allowed_domains = ['www.xiachufang.com']
    start_urls = ['http://www.xiachufang.com/category/51761/?page=10']

    def parse(self, response):
        # 写法1
        lists = response.xpath("//div[@class='recipe recipe-215-horizontal pure-g image-link display-block']")
        for element in lists:
            try:
                detail_url = element.xpath("div/p[@class='name']/a/@href").extract()[0]
                if detail_url:
                    yield Request(url=parse.urljoin(response.url, detail_url),
                                meta={"url": parse.urljoin(response.url, detail_url)},
                                callback=self.parse_detail)
            except Exception as e:
                print(e)
        # 写法2
        # url_lists=response.xpath("//div/p[@class='name']/a/@href").extract()
        # for url in url_lists:
        #    print(url)
        try:
            nextUrl = response.xpath("//div[@class='pager']/a[@class='next']/@href").extract()[0]
            if nextUrl:
                yield Request(url=parse.urljoin(response.url, nextUrl), callback=self.parse)
        except Exception as e:
            print(e)

    def parse_detail(self, response):
        item = KitchenItem()
        title = response.xpath("//h1[@class='page-title']/text()").extract()[0]
        topimg = response.xpath("//div[@class='cover image expandable block-negative-margin']/img/@src").extract()[0]
        # /html/body/div[4]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/span[1]
        try:
            score = response.xpath("//div[@class='score float-left']/span[@class='number']/text()").extract()[0]
        except Exception as e:
            score="0"
        cookcount = response.xpath("//div[@class='cooked float-left']/span[@class='number']/text()").extract()[0]
        author = response.xpath("//div[@class='author']/a/span/text()").extract()[0]
        author_img = response.xpath("//div[@class='author']/a/img/@src").extract()[0]
        try:
            one_message = response.xpath("//div[@class='desc mt30']/text()").extract()[0]
        except Exception as e:
            one_message=""
        tools_message = response.xpath("//div[@class='ings']/text()").extract()[0]
        message = response.xpath("//div[@class='steps']/text()").extract()[0]
        try:
            tip = response.xpath("//div[@class='tip']/text()").extract()[0]
        except Exception as e:
            tip=""
        try:
            video_url = response.xpath("//iframe/@src").extract()[0]
        except Exception as e:
            video_url=""
        url = response.meta.get("url", "")
        item["title"] = title
        item["create_date"] = ""
        item["topimg"] = topimg
        item["url"] = url
        item["object_id"] = gen_md5(url)
        item["score"] = score
        item["cookcount"] = cookcount
        item["author"] = author
        item["author_img"] = author_img
        item["desmessage"] = one_message
        item["imgsmessage"] = tools_message
        item["stepsmessage"] = message
        item["tip"] = tip
        item["videourl"] = video_url
        print(item)
        yield item
