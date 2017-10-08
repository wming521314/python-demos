# coding: utf-8
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy_douban.items import DoubanItem

from scrapy import optional_features
optional_features.remove('boto')

class Douban(CrawlSpider):
    name = "douban"
    redis_key = "douban:start_urls"
    start_urls = ["https://movie.douban.com/top250"]

    base_url = "https://movie.douban.com/top250"

    def parse(self, response):
        print response
        item = DoubanItem()
        selector = Selector(response)
        '''
        <li>
            <div class="item">
                <div class="pic">
                    <em class="">12</em>
                    <a href="https://movie.douban.com/subject/3793023/">
                        <img alt="三傻大闹宝莱坞" src="https://img3.doubanio.com/view/movie_poster_cover/ipst/public/p579729551.jpg" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/3793023/" class="">
                            <span class="title">三傻大闹宝莱坞</span>
                                    <span class="title">&nbsp;/&nbsp;3 Idiots</span>
                                <span class="other">&nbsp;/&nbsp;三个傻瓜(台)  /  作死不离3兄弟(港)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 拉库马·希拉尼 Rajkumar Hirani&nbsp;&nbsp;&nbsp;主演: 阿米尔·汗 Aamir Khan / 卡...<br>
                            2009&nbsp;/&nbsp;印度&nbsp;/&nbsp;剧情 喜剧 爱情 歌舞
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.1</span>
                                <span property="v:best" content="10.0"></span>
                                <span>676244人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">英俊版憨豆，高情商版谢耳朵。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
        '''
        movies = selector.xpath('//div[@class="info"]')

        for movie in movies:
            titles = movie.xpath('div[@class="hd"]/a/span/text()').extract()
            full_title =""
            for title in titles:
                full_title += title

            movie_info = movie.xpath('div[@class="bd"]/p/text()').extract()

            star = movie.xpath('div[@class="bd"]/div[@class="star"]/span["rating_num"]/text()').extract()[0]
            quote = movie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if quote:
                quote =quote[0]
            else:
                quote = ''

            item['title'] = full_title
            item['movieInfo'] = ";".join(movie_info)
            item['star'] = star
            item['quote'] = quote

            yield item
        '''
        <span class="next">
            <link rel="next" href="?start=25&amp;filter=">
            <a href="?start=25&amp;filter=">后页&gt;</a>
        </span>
        '''
        next_link = selector.xpath('//span[@class="next"]/link/@href').extract()
        #最后一页的next为空
        if next_link:
            next_link = next_link[0]
            print next_link # for debug
            yield Request(self.base_url + next_link, callback=self.parse)


if __name__ == "__main__":
    html_str = r'''
    <li>
        <div class="item">
            <div class="pic">
                <em class="">12</em>
                <a href="https://movie.douban.com/subject/3793023/">
                    <img alt="三傻大闹宝莱坞" src="https://img3.doubanio.com/view/movie_poster_cover/ipst/public/p579729551.jpg" class="">
                </a>
            </div>
            <div class="info">
                <div class="hd">
                    <a href="https://movie.douban.com/subject/3793023/" class="">
                        <span class="title">三傻大闹宝莱坞</span>
                                <span class="title">&nbsp;/&nbsp;3 Idiots</span>
                            <span class="other">&nbsp;/&nbsp;三个傻瓜(台)  /  作死不离3兄弟(港)</span>
                    </a>


                        <span class="playable">[可播放]</span>
                </div>
                <div class="bd">
                    <p class="">
                        导演: 拉库马·希拉尼 Rajkumar Hirani&nbsp;&nbsp;&nbsp;主演: 阿米尔·汗 Aamir Khan / 卡...<br>
                        2009&nbsp;/&nbsp;印度&nbsp;/&nbsp;剧情 喜剧 爱情 歌舞
                    </p>


                    <div class="star">
                            <span class="rating45-t"></span>
                            <span class="rating_num" property="v:average">9.1</span>
                            <span property="v:best" content="10.0"></span>
                            <span>676244人评价</span>
                    </div>

                        <p class="quote">
                            <span class="inq">英俊版憨豆，高情商版谢耳朵。</span>
                        </p>
                </div>
            </div>
        </div>
    </li>
    '''
    print html_str
    selector = Selector(html_str)
    movies = selector.xpath('//div[@class="info"]')
    for movie in movies:
        quote = movie.xpath('div[@class="bd"]/p/[@class="quote"]/span/text()').extract()
        print quote