# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：02-怎么测量一个数据类型是否可以迭代.py
@Author  ：DearMCgood
@Date    ：2022/5/6 10:47 
"""


from collections.abc import Iterable

print(isinstance("abc123", Iterable))
# >>> True
print(isinstance((), Iterable))
# >>> True
print(isinstance([], Iterable))
# >>> True
print(isinstance({}, Iterable))
# >>> True

print(isinstance(100, Iterable))
# >>> False
print(isinstance(1.1, Iterable))
# >>> False