# From the select result , we can see that every fetch is based on last result collection.
import MySQLdb

conn = MySQLdb.Connection(host="127.0.0.1",port=3306,user="root",passwd="root",db="python_mysql_test",charset="utf8")

cur = conn.cursor()

sql_str = "select * from user"
cur.execute(sql_str)

print cur.rowcount

rs = cur.fetchone()
print "fetchone:" + str(rs)

rs = cur.fetchmany(2)
print "fetchmany(2):" + str(rs)

rs = cur.fetchall()
print "fetchall:" + str(rs)

cur.close()
conn.close()