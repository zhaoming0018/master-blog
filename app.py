# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server
from handler.application import application
import init
from batch.create_db import create_database_blog
import sys
from optparse import OptionParser


def main():
    httpd = make_server('', init.PORT, application)
    print('Serving HTTP on port %s...' % init.PORT)
    httpd.serve_forever()


if __name__ == '__main__' :
    if len(sys.argv)>1 and sys.argv[1] == 'create':
        create_database_blog()
    else:
        main()