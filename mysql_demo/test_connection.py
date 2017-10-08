import MySQLdb

conn = MySQLdb.Connection(host="127.0.0.1",port=3306,user="root",passwd="root",db="python_mysql_test",charset="utf8")

cur = conn.cursor()

print conn
print cur

cur.close()
conn.close()