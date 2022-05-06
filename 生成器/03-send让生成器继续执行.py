# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：03-send让生成器继续执行.py
@Author  ：DearMCgood
@Date    ：2022/5/6 11:44 
"""


# send
# 如果想让生成器继续执行，我们可以使用next()或send()
# 相同点：都会让生成器向下执行，运行时，如果遇不到yield，会产生异常
# 不同点：next() 只会让运行继续开始，而 send() 除了可以 让其运行之外，还可以将某个数据携带过去

def generator_test():
    while True:
        print("----1----")
        num = yield 100
        print("----2----", "num=", num)


g = generator_test()
next(g)
next(g)


# >>> ----1----
# >>> ----2---- num= None
# >>> ----1----


def generator_test():
    while True:
        print("----1----")
        num = yield 100
        print("----2----", "num=", num)


g = generator_test()
# next(g)
print(g.send(None))
print(g.send(100))
# >>> ----1----
# >>> 100
# >>> ----2---- num= 100
# >>> ----1----
# >>> 100
