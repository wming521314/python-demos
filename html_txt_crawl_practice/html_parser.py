# coding: utf8
from bs4 import BeautifulSoup
import re

class HtmlParser(object):
    def parse(self, html_content):
        if html_content is None:
            return

        soup = BeautifulSoup(html_content, "lxml", from_encoding="utf-8")
        item_arr = [];

        tr_arr = soup.select("table.DefaultTable")[0].select("tr")
        #print(tr_arr)
        for i,tr in enumerate(tr_arr):
            item = {};
            if i<2:
                continue
            #print(tr)
            item['nickname'] = tr.select("a.WeixinNickname")[0].get_text()
            item['detail'] = tr.select("span.VoteOptionTitle")[0].get_text()
            item['roomnum'] = tr.select('span[id^="MainContent_rptLogList_lbCustomItemTitleAndContentList_"]')[0].get_text().split("：")[1]
            item_arr.append(item)
        #print(item_arr)
        return item_arr