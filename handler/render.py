# -*- coding:utf-8 -*-
from init import VIEW_PATH 
import os
def return_html(viewName, parameter=None, dirPath=''):
    if dirPath == '':
        path = os.path.join(VIEW_PATH,  viewName+ '.html')
    else:
        path = os.path.join(VIEW_PATH, dirPath, viewName, '.html')
    try:
        f = open(path,encoding='utf-8')
        result = f.read()
        if parameter != None:
            result = result % parameter
        return [bytes(result,"utf-8")]
    except IOError:
        raise IOError("文件%s读取错误" % path)
