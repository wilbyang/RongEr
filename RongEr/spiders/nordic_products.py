# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from RongEr.items import RongerItem
class NordicProductsSpider(CrawlSpider):
    name = "nordic_products"
    allowed_domains = ["livinorden.com"]
    start_urls = (
        'http://www.livinorden.com/adulthealproducts/adult_health_products.html',
    )
    rules = (
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('adulthealproducts\/adulthealproducts\/.*\.html', )), callback='parse_item'),
    )

    def parse_item(self, response):
        item = RongerItem()
        item['name'] = response.xpath("//div[@id='content']//h3/text()").extract()[0]
        descr = response.xpath("//div[@id='content']//*[local-name()='p' or local-name()='b']/text()").extract()
        item['description'] = ''.join(descr)
        item['image'] = response.xpath("//div[@id='content']//img/@src").extract()[0]
        item['largeImage'] = response.xpath("//div[@id='content']//img/@src").extract()[0]
        yield item
