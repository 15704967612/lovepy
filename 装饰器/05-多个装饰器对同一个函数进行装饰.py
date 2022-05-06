# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：05-多个装饰器对同一个函数进行装饰.py
@Author  ：DearMCgood
@Date    ：2022/5/6 10:29 
"""


# 多个装饰器对同一个函数进行装饰

def makeBold(fn):
    def warpped1():
        return "<b>" + fn() + "</b>"

    return warpped1


def makeItail(fn):
    def warpped2():
        return "<i>" + fn() + "</i>"

    return warpped2


# Python解释器发现装饰器下面不是跟着函数，还是一个装饰器，则跳过先执行下面的
# 多个装饰器对同一个函数进行装饰，由下往上执行
@makeBold  # 相当于 f1 = makeBold(f1)
@makeItail  # 相当于 f1 = makeItail(f1)
def f1():
    return "hwllo word-1"


# 最后 f1 指向了最上面的装饰器的内部函数 warpped1
print(f1())

# >>> <b><i>hwllo word-1</i></b>
