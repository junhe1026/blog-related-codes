# -*- coding: utf-8 -*-
"""
我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。
今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。
注：所给数据都有解，不用考虑无解的情况。

a = gcd(x,y)
b = lcm(x,y) = x*y/gcd(x,y) = x*y/a

-> x*y = a*b
"""

import math

def find_x_y(a,b):
    product = a*b
    match_num = []
    for i in range(1, int(math.sqrt(product))+1):
        if product % i == 0:
            match_num.append((i, product//i))

    min_num = (999, 999)
    for i, item in enumerate(match_num):
        if i == 0:
            min_num = item
        else:
            if sum(min_num) > sum(item):
                min_num = item

    print(min_num[0], ' ', min_num[1])


find_x_y(6, 858)


"""更优化解，从开方后的数向下解，明显减少循环"""
a = 858
b = 6
k = max(a,b) / min(a,b)
i = int(k ** 0.5)

while i > 0:
    if k % i == 0:
        print("%d %d" % (i*min(a,b),k*min(a,b)/i))
        break
    i -= 1
