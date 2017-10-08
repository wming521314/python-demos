# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_daomu_redis project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_daomu_redis'

SPIDER_MODULES = ['scrapy_daomu_redis.spiders']
NEWSPIDER_MODULE = 'scrapy_daomu_redis.spiders'

ITEM_PIPELINES = {'scrapy_daomu_redis.pipelines.ScrapyDaomuRedisPipeline':300}

USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
COOKIES_ENABLED=True
ROBOTSTXT_OBEY = True

'''
# 启用Redis调度存储请求队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPrioriyQueue"
# 确保所有的爬虫通过Redis去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# REDIS_URL = 'redis://root:@127.0.0.1:6379'
REDIS_URL = None
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
'''

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'dmbj_novel'
MONGODB_DOCNAME = 'book'

