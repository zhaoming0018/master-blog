# -*- coding:utf-8 -*-
import handler.getHandler as getHandler
import handler.postHandler as postHandler
from init import ROOT_PATH
import os
import base64
from imp import reload

def application(request, response):
    # environ中存储着请求信息，PATH_INFO表示请求路径
    method = request['REQUEST_METHOD']
    if method == 'GET':
        reload(getHandler)
        return getHandler.getHandler(request, response)
    elif method == 'POST':
        # 必须先执行下面的命令
        reload(postHandler)
        return postHandler.postHandler(request, response)