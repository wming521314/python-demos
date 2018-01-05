# coding: utf8
# import urllib2
from urllib.request import urlopen
import html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,path_arr):

        for path in path_arr:
            htmlfile = open(path, 'r')
            html_content = htmlfile.read()
            #print(html_content)
            data = self.parser.parse(html_content)
            self.outputer.setData(data)
            self.outputer.output_html()

if __name__ == "__main__":
    file_path_arr = ["Untitled-2.html"]
    obj_spider = SpiderMain()
    obj_spider.craw(file_path_arr)
