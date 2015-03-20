# -*- coding: utf-8 -*-

"""给你两个正整数a,b,  输出它们公约数的个数。"""

def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

a = 36
b = 24

r = gcd(a, b)
if a>b:
    print(len([i for i in range(1, gcd(a,b)+1) if a % i == 0 and b % i == 0]))
else:
    print(len([i for i in range(1, gcd(b,a)+1) if a % i == 0 and b % i == 0]))