# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：02-装饰带参数的函数.py
@Author  ：DearMCgood
@Date    ：2022/5/6 10:24 
"""


# 装饰带参数的函数
def sum(func):
    def inner(a, b):
        a += 5
        b += 3
        print("A=%d && B=%d" % (a, b))
        func(a, b)

    return inner


@sum
def cal(a, b):
    a -= 2
    b -= 1
    print("A=%d && B=%d" % (a, b))


cal(5, 8)


# >>> A=10 && B=11
# >>> A=8 && B=10