# coding: utf8

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open("output.html","w")
        fout.write("<html>")
        fout.write("<head>")
        fout.write('<meta charset="UTF-8" >')
        fout.write('<style>table,table tr th, table tr td { border:1px solid #0094ff; }</style>')
        fout.write("</head>")
        fout.write("<body>")
        fout.write('<table style="width=100%,border:1px solid;">')
        fout.write('<tr style="width:100%"><th style="width:10%">url</th><th style="width:5%">标题</th><th style="width:85%">摘要</th></tr>')
        for data in self.datas:
            fout.write('<tr style="width:100%"><td style="width:10%">'+data['url'].encode("utf-8")+'</td><td style="width:5%">'+data['title'].encode('utf-8')+'</td><td style="width:85%">'+data['summary'].encode('utf-8')+'</td></tr>')
        fout.write('</table>')
        fout.write("</body>")
        fout.write("</html>")