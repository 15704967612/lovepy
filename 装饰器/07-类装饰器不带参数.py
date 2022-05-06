# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：07-类装饰器不带参数.py
@Author  ：DearMCgood
@Date    ：2022/5/6 10:32 
"""


# 类装饰器不带参数

class Test(object):
    def __init__(self, func):
        print("-----初始化-----")
        print("函数名是 %s" % func.__name__)
        self.__func = func

    def __call__(self):
        print("-----装饰器中的功能-----")
        self.__func()


"""
说明
1、当用Test来做装饰器对test函数进行装饰的时候，
  a.首先会创建test的实例对象，并且会把test这个函数名传递到__init__方法中
  b.即在__init__方法中的属性__func指向了test指向的函数
2、test指向了用Test创建出来的实例对象
3、当在使用test()进行调用时，就相当于直接调用实例对象，因此会调用这个对象的__call__方法
4、为了能够在__call__方法中调用原来test指向的函数，所以在__init__方法中就需要一个实例属性来保存这个函数体的引用
   所以才有了self.__func = func 这句代码，从而在__call__方法中能够调用到test之前的函数体
"""


@Test    # 等价于 test = Test(test)
def test():
    print("-------test--------")


test()

# >>> -----初始化-----
# >>> 函数名是 test
# >>> -----装饰器中的功能-----
# >>> -------test--------
