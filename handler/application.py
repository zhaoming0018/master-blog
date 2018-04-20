# -*- coding:utf-8 -*-
from handler.getHandler import getHandler
from handler.postHandler import postHandler
from init import ROOT_PATH
import os
import base64

def application(request, response):
    # environ中存储着请求信息，PATH_INFO表示请求路径
    method = request['REQUEST_METHOD']
    if method == 'GET':
        response('200 OK', [('Content-Type', 'text/html')])
        return getHandler(request)
    elif method == 'POST':
        # 必须先执行下面的命令
        response('200 OK', [('Content-Type', 'text/html')])
        return postHandler(request)