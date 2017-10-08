# coding: utf8
from scrapy.spiders import  CrawlSpider
from scrapy.selector import Selector
from scrapy import Request
from scrapy_daomu.items import ScrapyDaomuItem

class spider(CrawlSpider):
    name = "novel"
    redis_key = "novel:start_urls"
    start_urls = ["http://www.daomubiji.com/"]

    def parse(self, response):
        print "aaaaaaaaaaaa"
        selector = Selector(response)
        book_urls = selector.xpath('//ul[@class="sub-menu"]/li/a/@href').extract()
        for book_url in book_urls:
            yield Request(book_url, callback=self.parse_sub_page,dont_filter=True)

    def parse_sub_page(self, response):
        selector = Selector(response)

        book_name = selector.xpath('//title/text()').extract()

        chapters = selector.xpath('//div[@class="excerpts"]')[0].xpath("article/a/text()").extract()
        chapter_urls = selector.xpath('//div[@class="excerpts"]')[0].xpath("article/a/@href").extract()

        for i in range(len(chapter_urls)):
            arr_tmp = chapters[i].split(" ")
            item = ScrapyDaomuItem()
            item['book_name'] = book_name
            item['chapter_num'] = arr_tmp[-2]
            item['chapter_name'] = arr_tmp[-1]
            item['chapter_url'] = chapter_urls[i]
            yield item