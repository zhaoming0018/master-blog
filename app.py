from wsgiref.simple_server import make_server
import yaml
import json

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # environ中存储着请求信息，PATH_INFO表示请求路径
    json.dumps(environ)
    result = bytes('<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web'),'utf-8')
    # 返回的结果必须是字节流
    return [result]


def main():
    # 读取配置文件
    f = open("config.yml")
    x = yaml.load(f)
    httpd = make_server('', x['port'], application)
    print('Serving HTTP on port %s...' % x['port'])
    httpd.serve_forever()


if __name__ == '__main__' :
    main()
