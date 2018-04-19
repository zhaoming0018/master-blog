# -*- coding:utf-8 -*-
from handler.getHandler import getHandler
from handler.postHandler import postHandler

def application(environ, start_response):
    
    # environ中存储着请求信息，PATH_INFO表示请求路径
    method = environ['REQUEST_METHOD']
    if method == 'GET':
        try:
            start_response('200 OK', [('Content-Type', 'text/html')])
            return getHandler(environ)
        except IOError as e:
            pass
        
    if method == 'POST':
        # 必须先执行下面的命令
        start_response('200 OK', [('Content-Type', 'text/html')])
        return postHandler(environ)