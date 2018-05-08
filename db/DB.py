# -*- coding:utf-8 -*-
from init import DB_PATH
import sqlite3
import os
class DB:
    dbname = None
    conn = None
    def __init__(self):
        pass
    
    def __del__(self):
        self.conn = None

    """
    连接数据库，connect(dbname)
    内部程序完成连接的切换
    """
    def connect(self, dbname):
        # 检查数据库名和连接状态
        url = os.path.join(DB_PATH, dbname+ '.db3')
        if dbname == self.dbname:
            if self.conn == None:
                self.conn = sqlite3.connect(url)
        else:
            if self.conn == None:
                self.dbname = dbname
                self.conn = sqlite3.connect(url)
            else:
                self.conn.close()
                self.conn = sqlite3.connect(url) 

        print("连接到数据库文件：%s" % url)

    def execute_sql(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        print(sql)
    
    def find_sql(self, sql):
        cur = self.conn.cursor()
        c = cur.execute(sql)
        result = []
        for row in c:
            result.append(row)
        self.conn.commit()
        print(sql)
        return result

    def dict_factory(self, cursor, row): 
        d = {} 
        for idx, col in enumerate(cursor.description): 
            d[col[0]] = row[idx] 
        return d

    def find_dict(self, sql):
        self.conn.row_factory = self.dict_factory
        cur = self.conn.cursor()
        c = cur.execute(sql)
        result = [] 
        for row in c:
            result.append(row)
        self.conn.commit()
        print(sql)
        return result

    

db = DB()