from cgitb import text
import datetime
from ntpath import join
from urllib.parse import urlparse, urljoin
import socket
import scrapy

from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader

from vietnamnet.items import VietnamnetItem
from scrapy.http import Request


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['vietnamnet.vn']
    start_urls = [
        "https://vietnamnet.vn/vn/thoi-su/",
        "https://vietnamnet.vn/vn/the-thao/",
        "https://vietnamnet.vn/vn/giao-duc/",
        "https://vietnamnet.vn/vn/phap-luat/",
        "https://vietnamnet.vn/vn/cong-nghe/",
        "https://vietnamnet.vn/vn/oto-xe-may/"
    ]
    
    def parse(self, response):
        next_urls = [urljoin(response.url, i) for i in
                     response.xpath('//link[@rel="next"]/@href').extract()]
        for url in next_urls:
            yield Request(url)
        next_items = [urljoin(response.url, i) for i in
                      response.xpath('//div[@class="feature-box"]//h3/a/@href').extract()]
        for url in next_items:
            self.log(url)
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        # Create the loader using the response
        l = ItemLoader(item=VietnamnetItem(), response=response)

        # Load fields using XPath expressions
        l.add_value('loai', response.xpath('//div[@class="breadcrumb-box__link "]//p/a[1]/text()').extract(), Join(), MapCompose(str.strip))

        l.add_value('thoigian', response.xpath('//div[@class="breadcrumb-box__time"]//p/span/text()').extract(), Join(), MapCompose(str.strip), MapCompose(lambda i: i.replace('\xa0',' ')))

        l.add_value('tieude', response.xpath('//div[@class="newsFeature__header"]//h1/text()').extract())
        
        l.add_value('doandan', response.xpath('//div[@class="newFeature__main-textBold"]//text()').extract(), Join('\n'), MapCompose(str.strip))

        l.add_value('noidung', response.xpath('//*[@id="maincontent"]/div/p/text()').extract(),Join('\n'),MapCompose(lambda i: i.replace('&ndsp;',' ')), MapCompose(lambda i: i.replace('\n',' ')), MapCompose(lambda i: i.replace('\xa0',' ')), MapCompose(str.strip) )
        
        l.add_value('linkanh', response.xpath('//*[@id="maincontent"]/div/figure/img/@src').extract())

        l.add_value('tags', response.xpath('//div[@class="list-tag-related"]//ul/li/a/text()').extract())

        l.add_value('tacgia',response.xpath('//strong/text()').extract(), MapCompose(lambda i: i.replace('\xa0',' ')))

        l.add_value('like',response.xpath('//div[@class="newsFeature__header"]//div/a[1]/span[2]/text()').extract())

        l.add_value('url', response.url)
        
        return l.load_item()
