# coding: utf8

class HtmlOutputer(object):
    def __init__(self):
        self.data =[]

    def setData(self,data):
        self.data = data

    def output_html(self):
        fout = open("output.html","w")
        fout.write("<html>")
        fout.write("<head>")
        fout.write('<meta charset="UTF-8" >')
        fout.write('<style>table,table tr th, table tr td { border:1px solid #0094ff; }</style>')
        fout.write("</head>")
        fout.write("<body>")
        fout.write('<table style="width=100%,border:1px solid;">')
        fout.write('<tr style="width:100%"><th style="width:20%">昵称</th><th style="width:50%">详情</th><th style="width:30%">房间号</th></tr>')
        for item in self.data:
            fout.write('<tr style="width:100%"><td style="width:20%">'+item['nickname']+'</td><td style="width:50%">'+item['detail']+'</td><td style="width:30%">'+item['roomnum']+'</td></tr>')
        fout.write('</table>')
        fout.write("</body>")
        fout.write("</html>")