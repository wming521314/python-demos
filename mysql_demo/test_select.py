# -*- coding: UTF-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import MySQLdb

conn = MySQLdb.Connection(host="127.0.0.1",port=3306,user="root",passwd="root",db="python_mysql_test",charset="utf8")

cur = conn.cursor()

sql_str = "select * from user"

cur.execute(sql_str)

rs = cur.fetchall()
for row in rs:
    print "id = %d , name = %s" % row

cur.close()
conn.close()