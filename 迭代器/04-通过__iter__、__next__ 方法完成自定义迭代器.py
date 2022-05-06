# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：04-通过__iter__、__next__ 方法完成自定义迭代器.py
@Author  ：DearMCgood
@Date    ：2022/5/6 10:55 
"""

from collections.abc import Iterable
from collections.abc import Iterator


class MyList(object):
    """自定义一个可迭代对象"""

    def __init__(self):
        self.container = []

    def add(self, item: int):
        self.container.append(item)

    def __iter__(self):
        # 这个方法有两个功能
        # 1、标记当前创建出来的对象一定是 可迭代对象
        # 2、当调用iter()函数的时候，这个方法会被自动调用，它返回 自己指定的那个 迭代器
        return MyIterator()


class MyIterator(object):
    def __init__(self):
        pass

    def __next__(self):
        # 这个方法可以有2个功能
        # 1、标记当前类创建出来的对象(当然了还必须有__iter__方法)一定是 迭代器
        # 2、当调用next()函数的时候 这个方法会被自动调用，它返回一个数据
        print("hello word")
        return 100

    def __iter__(self):
        pass


mylist = MyList()  # 可迭代对象
# 用iter(mylist)就是获取 mylist 这个可迭代对象的 迭代器，它会自己调用这个mylist这个对象的__iter__方法
# 这个方法返回 东西就当作iter()函数的返回值，就是迭代器

mylist_iter = iter(mylist)  # 迭代器

print("mylist是否是可以迭代对象", isinstance(mylist, Iterable))
# >>> mylist是否是可以迭代对象 True
print("mylist是否是迭代器", isinstance(mylist, Iterator))
# >>> mylist是否是迭代器 False

print("mylist_iter是否可迭代对象", isinstance(mylist_iter, Iterable))
# >>> mylist_iter是否可迭代对象 True
print("mylist_iter是否是迭代器", isinstance(mylist_iter, Iterator))
# >>> mylist_iter是否是迭代器 True


# 小总结
# 如果定义类时，有__iter__方法，那么这个类创建出来的对象一定是 可迭代对象
# 迭代器 一定是 可迭代对象，可迭代对象 不一定 是迭代器
