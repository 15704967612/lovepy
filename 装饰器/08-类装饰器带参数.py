# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：08-类装饰器带参数.py
@Author  ：DearMCgood
@Date    ：2022/5/6 10:36 
"""


# 类装饰器带参数

class Test(object):
    def __init__(self, num):
        print("-----init-----")
        self.__num = num

    def __call__(self, func):
        print("-----call-----")
        self.__func = func
        return self.call_old_func

    def call_old_func(self):
        print("开启调用装饰器修饰功能的函数1")
        print(self.__num)
        self.__func()
        print("开启调用装饰器修饰功能的函数2")


@Test(100)
def f1():
    print("------f1--------")

# >>> -----init-----
# >>> -----call-----
# >>> 开启调用装饰器修饰功能的函数1
# >>> 100
# >>> ------f1--------
# >>> 开启调用装饰器修饰功能的函数2


# 装饰器总结
# 1、装饰器：能够快速将函数的指向修改，能够在不修改代码的前提下，给函数添加功能的方式
# 2、装饰器功能：给函数添加功能
# 3、特点：不修改原函数代码，还能添加功能；只能在原函数执行之前或者执行之后添加，不能在原函数运行一半时添加
# 4、实现过程：1）将原函数的引用当作实参传递到闭包中 2）修改原函数的指向为闭包中的内部函数
# 5、装饰器实际用到了闭包，只不过在给外层函数传递参数时，传递的是需要被装饰得函数的引用而已
# 6、装饰器还用到了引用，即在python中，a=xxx 那么无论 xx 是列表、字典还是对象，一定是a指向它，而不是存储它
