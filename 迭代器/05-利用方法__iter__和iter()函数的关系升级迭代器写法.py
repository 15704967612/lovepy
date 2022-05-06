# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：05-利用方法__iter__和iter()函数的关系升级迭代器写法.py
@Author  ：DearMCgood
@Date    ：2022/5/6 11:06 
"""

"""

__iter__ 方法 和 iter()函数的关系:
当一个可迭代对象调用iter()函数时，它会自动调用这个可迭代对象的__iter__方法，这个方法的返回值的对象当作迭代器

__next__ 和 next()函数的关系:
当对一个迭代器对象调用next()函数时，它会自动调用这个迭代器对象的__next__方法，这个方法返回想要的那个数据

"""


class MyList(object):
    """自定义一个可迭代对象"""

    def __init__(self):
        self.items = []
        self.current = 0

    def add(self, val):
        self.items.append(val)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.items):
            item = self.items[self.current]
            self.current += 1
            return item
        else:
            """
            return None
            为什么一定要抛出StopIteration异常，而不使用返回进行判断?
            因为在使用for循环遍历可迭代对象时，for循环内部实现了对该StopIteration异常的处理，
            如果使用自定处理方法，for循环将无法感知，陷入死循环，除非不用for循环     
            """
            self.current = 0     # 解决第二次对mylist可迭代对象进行for的时候，不循环的问题
            raise StopIteration  # 抛出异常


if __name__ == '__main__':
    mylist = MyList()  # 可迭代对象
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    mylist.add(5)

    for num in mylist:
        print(num)

    for num in mylist:
        print(num)
    # 为什么第二次对mylist使用for循环的时候，反而不循环了呢？

    # 除了for循环能接收可迭代对象，list、tuple等也可以接收
    num = list(mylist)
    print(num)
    # >>> [1, 2, 3, 4, 5]
