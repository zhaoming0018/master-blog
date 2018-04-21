# -*- coding:utf-8 -*-
from init import VIEW_PATH
import handler.handler as handler
import urllib
import json
from db.DB import db
import os

def getHandler(environ):
    query_string = environ['QUERY_STRING']
    parse_query = urllib.parse.parse_qs(query_string)
    pathinfo = environ['PATH_INFO']
    print("pathinfo 是："+pathinfo)
    if pathinfo == '/user/register':
        return handler.return_html('register')
    elif pathinfo == '/article/list':
        return handler.return_html('article_list')
    
    elif pathinfo == '/api/user/list':
        db.connect('blog')
        sql = """
            select userid,username,email,create_time,valid
            from user
        """
        rows = db.find_sql(sql)
        str = json.dumps(rows)
        return [bytes(str,"utf-8")]
    elif pathinfo == '/api/article/list':
        db.connect('blog')
        sql = """
            select articleid,title,tags,likes_num,dislikes_num,mark,create_time,valid
            from article
        """
        rows = db.find_sql(sql)
        str = json.dumps(rows)
        return [bytes(str,"utf-8")]
    elif pathinfo == '/article/edit':
        return handler.return_html('article_edit')
    elif pathinfo == '/user/list':
        return handler.return_html('user_list')
    elif pathinfo == '/':
        return handler.return_html('index')  
    elif pathinfo == '/user/login':
        return handler.return_html('login')
    elif pathinfo == '/user/aaa':
        return handler.return_html('aaa')
    elif pathinfo == '/api/article/show':
        articleid = parse_query['id'][0]
        db.connect("blog")
        sql = """
            SELECT TITLE,AUTHORID,CREATE_TIME,CONTENT 
            FROM ARTICLE
            WHERE ARTICLEID = %s
        """ % articleid
        rows = db.find_sql(sql)
        str = json.dumps(rows[0])
        return [bytes(str,"utf-8")]
    elif pathinfo == '/article/show':
        return handler.return_html('article_show')
    else:
        return [bytes("","utf-8")]
