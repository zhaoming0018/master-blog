# -*- coding:utf-8 -*-
"""
此脚本用于：
1. 设定一些网站系统常量
2. 读取配置文件
"""

import os
import yaml

# 版本说明：
# 格式为x.y.z
VERSION = "0.0.1"
# 根目录
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
# 数据库文件所在目录
DB_PATH = os.path.join(ROOT_PATH, "db\\")
# 模板文件所在目录
VIEW_PATH = os.path.join(ROOT_PATH,"view\\")

# 读取配置文件
file = open("config.yml")
config = yaml.load(file)
PORT = config['port']