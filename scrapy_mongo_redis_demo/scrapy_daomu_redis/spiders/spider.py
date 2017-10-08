# coding: utf8

from scrapy_redis.spiders import RedisSpider
from scrapy.spiders import  CrawlSpider
from scrapy.selector import Selector
from scrapy import Request
from scrapy_daomu_redis.items import ScrapyDaomuRedisItem


class spider(CrawlSpider):
    name = "daomu"
    redis_key = "daomu:start_urls"
    start_urls = [
                    "http://www.daomubiji.com/",
                    # "http://www.daomubiji.com/qi-xing-lu-wang-01.html",
                 ]

    def parse(self, response):
        selector = Selector(response)
        book_urls = selector.xpath('//ul[@class="sub-menu"]/li/a/@href').extract()
        for book_url in book_urls:
            yield Request(book_url, callback=self.parse_sub_page)

    def parse_sub_page(self, response):
        selector = Selector(response)

        book_name = selector.xpath('//title/text()')[0].extract()

        chapters = selector.xpath('//div[@class="excerpts"]')[0].xpath("article/a/text()").extract()
        chapter_urls = selector.xpath('//div[@class="excerpts"]')[0].xpath("article/a/@href").extract()

        for i in range(len(chapter_urls)):
            print "chapter url : " + chapter_urls[i]
            arr_tmp = chapters[i].split(" ")
            item = ScrapyDaomuRedisItem()
            item['book_name'] = book_name
            item['chapter_num'] = arr_tmp[-2]
            item['chapter_name'] = arr_tmp[-1]
            item['chapter_url'] = chapter_urls[i]

            # yield item
            yield Request(chapter_urls[i], callback=self.parse_chapter_content, meta={"item": item})

    def parse_chapter_content(self,response):
        selector = Selector(response)
        item = response.meta['item']
        #<article class="article-content">
        chapter_content = selector.xpath('//article[@class="article-content"]')[0].xpath("p/text()").extract()
        chapter_content = "".join(chapter_content)
        item['chapter_content'] = chapter_content
        print chapter_content
        yield item
