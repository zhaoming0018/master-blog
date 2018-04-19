# -*- coding:utf-8 -*-
from init import VIEW_PATH
import handler.handler as handler
import urllib
from db.DB import db
import os

def getHandler(environ):
    query_string = environ['QUERY_STRING']
    parse_query = urllib.parse.parse_qs(query_string)
    pathinfo = environ['PATH_INFO']
    print("pathinfo 是："+pathinfo)
    if pathinfo == '/user/register':
        return handler.return_html('register')
    elif pathinfo == '/article/edit':
        return handler.return_html('article_edit')
    elif pathinfo == '/':
        return handler.return_html('index')  
    elif pathinfo == '/user/login':
        return handler.return_html('login')
    elif pathinfo == '/user/aaa':
        return handler.return_html('aaa')
    elif pathinfo == '/article/show':
        articleid = parse_query['id'][0]
        db.connect("blog")
        sql = """
            SELECT TITLE,AUTHORID,CREATE_TIME,CONTENT 
            FROM ARTICLE
            WHERE ARTICLEID = %s
            """ % articleid
        result = db.find_sql(sql)
        print(result)
        return handler.return_html('article_show',result[0])
    else:
        return [bytes("","utf-8")]
