# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：01-什么是闭包.py
@Author  ：DearMCgood
@Date    ：2022/5/6 11:45 
"""

"""
@闭包
在一个函数中返回另外一个函数的引用，只不过被返回函数用到了其它函数中的变量而且。
说到底就是只要用一个变量就可以指向某个函数代码块，就可以调用它。
"""


def make_pencli(color):
    def wtite(context):
        print("正在使用(%s)色，写: %s" % (color, context))

    return wtite


# 闭包1
black_pencil = make_pencli("黑")
black_pencil("我是喝墨水长大的")
# 闭包2
black_pencil = make_pencli("红")
black_pencil("这么巧，我也是，是不过是红墨水")

# >>> 正在使用(黑)色，写: 我是喝墨水长大的
# >>> 正在使用(红)色，写: 这么巧，我也是，是不过是红墨水
