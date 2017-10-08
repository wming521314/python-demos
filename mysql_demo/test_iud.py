# -*- coding: UTF-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import MySQLdb

conn = MySQLdb.Connection(host="127.0.0.1",port=3306,user="root",passwd="root",db="python_mysql_test",charset="utf8")

cur = conn.cursor()

sql_insert_str = "insert into user(id,name) values(4,'haha'),(5,'alice'),(6,'susan')"
sql_update_str = "update user set name='lisa' where id = 2"
sql_delete_str = "delete from user where id = 2"
try:
    cur.execute(sql_insert_str)
    cur.execute(sql_update_str)
    cur.execute(sql_delete_str)
except Exception as e:
    print e
    conn.rollback()

print cur.fetchall()

cur.close()
conn.close()