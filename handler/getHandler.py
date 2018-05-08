# -*- coding:utf-8 -*-
from init import VIEW_PATH
import handler.render as render
import urllib
import json
from db.DB import db
import os

def article_edit():
    return render.return_html('article_edit')

def routerRegister(router):
    routers = {
        "/article/edit" :  article_edit
    }
    return routers[router]()

def getHandler(environ, response):
    response('200 OK', [('Content-Type', 'text/html')])
    query_string = environ['QUERY_STRING']
    parse_query = urllib.parse.parse_qs(query_string)
    pathinfo = environ['PATH_INFO']
    print("pathinfo 是："+pathinfo)
    if pathinfo == '/user/register':
        return render.return_html('register')
    elif pathinfo == '/article/list':
        return render.return_html('article_list')
    elif pathinfo == '/article/modify':
        return render.return_html('article_modify')
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
        return routerRegister(pathinfo)
    elif pathinfo == '/user/list':
        return render.return_html('user_list')
    elif pathinfo == '/':
        return render.return_html('index')  
    elif pathinfo == '/user/login':
        return render.return_html('login')
    elif pathinfo == '/user/aaa':
        return render.return_html('aaa')
    elif pathinfo == '/api/article/show':
        articleid = parse_query['id'][0]
        db.connect("blog")
        sql = """
            SELECT TITLE,AUTHORID,CREATE_TIME,CONTENT 
            FROM ARTICLE
            WHERE ARTICLEID = %s
        """ % articleid
        rows = db.find_dict(sql)
        str = json.dumps(rows[0])
        return [bytes(str,"utf-8")]
    elif pathinfo == '/api/article/get':
        articleid = parse_query['id'][0]
        db.connect("blog")
        sql = """
            SELECT TITLE,TAGS,AUTHORID,CREATE_TIME,CONTENT 
            FROM ARTICLE
            WHERE ARTICLEID = %s
        """ % articleid
        rows = db.find_dict(sql)
        str = json.dumps(rows[0])
        return [bytes(str,"utf-8")]
    elif pathinfo == '/article/show':
        return render.return_html('article_show')
    else:
        return [bytes("","utf-8")]
