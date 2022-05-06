# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：03-装饰不带返回值的函数.py
@Author  ：DearMCgood
@Date    ：2022/5/6 10:26 
"""


# 装饰不带返回值的函数

def general(func):
    def xxx(*args, **kwargs):  # 用于接收不确定个数的参数
        func(*args, **kwargs)  # 将接收到的参数 进行拆包，然后返回给原函数

    return xxx


@general
def a(num):
    print("-------1", num)


a(100)


@general
def b(num, num2):
    print("-------2", num, num2)


b(100, 200)


@general
def c(num, num2, num3):
    print("-------1", num, num2, num3)


c(100, 200, 300)

# >>> -------1 100
# >>> -------2 100 200
# >>> -------1 100 200 300
