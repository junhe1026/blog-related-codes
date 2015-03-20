# -*- coding: utf-8 -*-
"""最简单的tornado hello word， 测试其异步特性"""

import logging
from tornado import web, ioloop, httpserver, autoreload, httputil
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.web import url, RequestHandler
from tornado.gen import coroutine


class ReqHander(RequestHandler):
    """request handler"""
    @coroutine
    def get(self):
        print(self.request.headers['Cookie'][:10], 'new get')
        url = 'http://www.baidu.com'
        method = 'GET'
        headers = httputil.HTTPHeaders(
            {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'}
        )
        request = HTTPRequest(url=url, method=method,
                              body=None, headers=headers)
        http_client = AsyncHTTPClient()
        resp = yield http_client.fetch(request)
        print(self.request.headers['Cookie'][:10], 'a')

        self.write(resp.body)


if __name__ == '__main__':
    """simple tornado server"""

    from tornado.options import options
    options.parse_command_line(final=True)  # 读取命令行参数
    options.parse_config_file('./conf.py', final=True)
    options.define('app_port', 6966)

    handler = {
        url(r'/index', ReqHander),
        url(r'.*', ReqHander)
    }

    settings = {
        'debug': True
    }

    app = web.Application(handler, **settings)
    app.listen(options.app_port)

    # 重新加载处理函数
    def reload():
        logging.info('reload')
        pass
    autoreload.add_reload_hook(reload)

    logging.info('server starts on port %s', options.app_port)
    ioloop.IOLoop.instance().start()
