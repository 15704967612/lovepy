# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：04-装饰带返回值的函数.py
@Author  ：DearMCgood
@Date    ：2022/5/6 10:28 
"""


# 装饰带返回值的函数，****通用装饰器******

def xxx(func):
    def yyy(*args, **kwargs):        # 用于接收不确定个数的参数
        ret = func(*args, **kwargs)  # 将接收到的参数 进行拆包，然后返回给原函数
        return ret                   # 这个return会在调用函数时，将原函数的结果返回到调用函数的地方

    return yyy                       # 这个return会在执行装饰器的过程，返回 内部函数yyy


@xxx
def a(num):
    print("-------1", num)
    return 200


a = a(100)
print(a)

# >>> -------1 100
# >>> 200
