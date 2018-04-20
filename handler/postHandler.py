# -*- coding:utf-8 -*-
import yaml
import json
import urllib
import sqlite3
from db.DB import db
def postHandler(environ):
    # 做GET和POST请求的解析
    query_string = environ['QUERY_STRING']
    parse_query = urllib.parse.parse_qs(query_string)
    parse_body = {} 
    try:  
        request_body_size = int(environ.get('CONTENT_LENGTH', 0)) 
        body = environ['wsgi.input'].read(request_body_size).decode()
        print(body)
        parse_body = urllib.parse.parse_qs(body) 
        print(parse_body)
    except (ValueError):  
        pass
    # 根据路由不同，处理请求
    pathinfo = environ['PATH_INFO']
    if pathinfo == '/article/add':
        title = parse_body['title'][0]
        tags = parse_body['tags'][0]
        authorid = 0
        content = parse_body['content'][0]
        mark = 'HOT'
        sql = """
            INSERT INTO ARTICLE(CREATE_TIME,TITLE,TAGS,AUTHORID,CONTENT,MARK)
             VALUES (datetime('now', 'localtime'), '%s', '%s', %s, '%s', '%s')
             """ % (title, tags, authorid, content, mark)
        db.connect('blog')
        db.execute_sql(sql)
        result = 'ok'
    if pathinfo == '/user/doRegister':
        username = parse_body['username'][0]
        password = parse_body['password'][0]
        confirm  = parse_body['confirm'][0]
        email = parse_body['email'][0]
        if password == confirm:
            db.connect('blog')
            sql = """
            INSERT INTO user(username,password,email,create_time)
            values ('%s', '%s','%s',datetime('now', 'localtime')) """ %(username, password,email)
            db.execute_sql(sql)
            result = "OK"
        else :
            result = "NO"
        
    if pathinfo == '/user/doLogin':
        username = parse_body['username'][0]
        password = parse_body['password'][0]
        # 数据库查找信息
        sql = "SELECT username,password FROM user WHERE username='%s' AND password = '%s'"% (username,password)
        db.connect("blog")
        res = db.find_sql(sql)
        print(res)
        if len(res) == 1:
            print(res)
            result = "OK"
        else:
            result = "NO"
        print(result)
    return [bytes(result,"utf-8")]