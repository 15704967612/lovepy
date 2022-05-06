# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：01-装饰器.py
@Author  ：DearMCgood
@Date    ：2022/5/6 10:19 
"""

"""
@装饰器
将函数作为参数传递给另外一个函数，返回一个新的地址指向该函数
"""


# 装饰不带参数的函数
def check_login(func):
    def inner():
        # 验证1
        print("人生苦短，我爱Python")
        # 验证2
        # 验证3
        func()
        print("爱学习")

    return inner


"""
装饰器的执行过程:
第一步
    当Python解释器遇到@check_login，将check_login当作可执行对象check_login()
    将f1函数当作实参进行传递，此时变成了check_login(f1)
第二步
    将check_login(f1)执行的返回值，当作新的f1的值，即此时 f1 = check_login(f1)
    也就是说 f1 的指向变成了check_login的返回值
"""


@check_login
def f1():
    print("HelloWord")


f1()

# >>> 人生苦短，我爱Python
# >>> HelloWord
# >>> 爱学习
