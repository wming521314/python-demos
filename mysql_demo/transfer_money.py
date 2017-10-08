# -*- coding: UTF-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import MySQLdb
class TransterMoney(object):
    def __init__(self,conn):
        self.conn = conn
    def transfer(self,source_id,target_id,money):
        try:
            self.check_source_available(source_id)
            self.check_source_available(target_id)
            self.has_enough_money(source_id,money)
            self.reduce_money(source_id,money)
            self.add_money(target_id,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback
            raise e
    def check_source_available(self,acc_id):
        cur = self.conn.cursor()
        try:
            sql = "select * from account where acc_id=%s" % acc_id
            print "check_source_available:"+sql
            cur.execute(sql)
            rs = cur.fetchall()
            if len(rs) !=1:
                raise Exception("账号%s不存在!" % acc_id)
        finally:
            cur.close()

    def has_enough_money(self,acc_id,money):
        cur = self.conn.cursor()
        try:
            sql = "select * from account where acc_id=%s and money>=%s" % (acc_id,money)
            print "has_enough_money : " + sql
            cur.execute(sql)
            rs = cur.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s没有足够的钱!" % acc_id)
        finally:
            cur.close()
    def reduce_money(self,acc_id,money):
        cur = self.conn.cursor()
        try:
            sql = "update account set money=money-%s where acc_id=%s" % (money,acc_id)
            print "reduce_money : " + sql
            cur.execute(sql)
            if cur.rowcount != 1:
                raise Exception("账号%s减款失败!" % acc_id)
        finally:
            cur.close()
    def add_money(self,acc_id,money):
        cur = self.conn.cursor()
        try:
            sql = "update account set money=money+%s where acc_id=%s" % (money,acc_id)
            print "reduce_money : " + sql
            cur.execute(sql)
            if cur.rowcount != 1:
                raise Exception("账号%s加款失败!" % acc_id)
        finally:
            cur.close()

if __name__ == "__main__":
    source_id = sys.argv[1]
    target_id = sys.argv[2]
    money = sys.argv[3]
    conn = MySQLdb.Connection(host="127.0.0.1",port=3306,user="root",passwd="root",db="python_mysql_test",charset="utf8")
    tr_money = TransterMoney(conn)

    try:
        tr_money.transfer(source_id,target_id,money)
    except Exception as e:
        print str(e)
    finally:
        conn.close()