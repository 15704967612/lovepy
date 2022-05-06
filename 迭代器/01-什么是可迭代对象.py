# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：01-什么是可迭代对象.py
@Author  ：DearMCgood
@Date    ：2022/5/6 10:45 
"""

"""
@迭代器 iterable
在实际工作中，经常需要快速将对象转化为其它不同的数据类型，此时如果可以快速遍历出自定义的对象，那么就可以大大减少代码的冗余
1、什么是迭代？迭代是访问集合元素的一种方式
2、什么是可迭代对象？只要是能用for循环遍历的都是可迭代对象
3、可迭代数据类型：[字符串、元组、列表、字典] 不可迭代数据类型：[整数、浮点数]对象。迭代器对象从第一个元素开始访问
4、迭代器是一个可以记住遍历位置的，直到所有的元素都被访问完结束。迭代器只能往前不会会退。
5、迭代对象的本质：
  1) 分析 可迭代对象 进行迭代的的过程，发现每迭代一次（即 for ... in ... 每循环一次）都会返回对象中的下一条数据，
     一直向后读取数据直到迭代了所有的数据后结束。
  2) 那么，在这个过程中应该有一个“人”去记录每次访问到了第几条数据，以便每次迭代都可以返回下一条数据。
     我们把这个能帮我们进行数据迭代的人“人”称为 迭代器（iterator）
  3) list、tuple等都是可迭代对象，我们可以通过 iter() 函数获取这些可迭代对象的迭代器，
     然后我们可以对获取到的迭代器不断使用 next() 函数来获取下一条数据。
------------------------------------------------
"""


class StuSystem:
    def __init__(self):
        self.stu_status = []

    def add(self):
        name = input("请输入学生姓名: ")
        tel = input("请输入学生联系方式: ")
        address = input("请输入学生地址: ")

        new_stu = dict()
        new_stu['name'] = name
        new_stu['tel'] = tel
        new_stu['address'] = address

        self.stu_status.append(new_stu)


# 创建管理系统对象
stu_sys = StuSystem()

# 添加三个学生到系统中
stu_sys.add()
stu_sys.add()
stu_sys.add()

# 问题：怎样才能实现用for循环遍历系统中所有学生的信息呢？下面的方式能实现吗？
for temp in stu_sys:
    print(temp)

# >>>    for temp in stu_sys:
# >>> TypeError: 'StuSystem' object is not iterable
