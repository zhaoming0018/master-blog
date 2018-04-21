# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server
from handler.application import application
from init import PORT
from batch.create_db import create_database_blog
import sys
from optparse import OptionParser


def main():
    httpd = make_server('', PORT, application)
    print('Serving HTTP on port %s...' % PORT)
    httpd.serve_forever()


if __name__ == '__main__' :
    if len(sys.argv)>1 and sys.argv[1] == 'create':
        create_database_blog()
    else:
        main()