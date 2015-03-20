# -*- coding: utf-8 -*-

"""用multiprocess 多进程同时发请求，测试tornado框架的异步性"""
import logging
import multiprocessing
import os
from urllib import request


def to_req(pname):
    c = 'pro: {0}, pid: {1}'.format(pname, os.getpid())
    logging.info(c)
    headers = {'Cookie': c}
    req = request.Request('http://127.0.0.1:6966/index', headers=headers)
    res = request.urlopen(req)
    print(res.headers)


record = []
if __name__ == '__main__':
    for i in range(4):
        process = multiprocessing.Process(target=to_req, args=('p%d' % i, ))
        process.start()
        record.append(process)

    for process in record:
        process.join()

"""
output:
pro: p0, p new get
pro: p2, p new get
pro: p1, p new get
pro: p3, p new get
pro: p0, p a
pro: p3, p a
pro: p2, p a
pro: p1, p a

可以发现，非线性输出，乱序返回。体现了tornado框架non-blocking async的特性
"""
