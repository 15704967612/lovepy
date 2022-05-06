# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：02-通过yield创建生成器.py
@Author  ：DearMCgood
@Date    ：2022/5/6 11:40 
"""

"""
通过 yield
generator功能非常强大
如果推荐的算法比较复杂，用类似列表生成式的 for 循环无法实现的时候，还可以使用之前学习的函数来实现一个生成器
下面以 斐波那契数列 举例
斐波那契数列指定是 [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, .....]
这个数列从第三项开始，每一项都等于前面两项之和
"""


# 生成器实现
def fib_generator():
    num1 = 1
    num2 = 1
    while True:
        temp_num = num1
        num1, num2 = num2, num1 + num2
        yield temp_num  # 只要函数中有yield，不管是否有return，那么这个函数一定是生成器


fib = fib_generator()  # 此时fib不在是一个普通的函数，而是一个生成器对象
                       # <generator object fib_generator at 0x106d7e150>

num1 = next(fib)  # 又因为生成器又是特殊的迭代器，所有可以使用next()、for循环取值
num2 = next(fib)

"""
yield 关键字
上面的代码，在函数中使用了 yield 关键字，替换了return， 虽然看上去仅仅是关键字不同，但是功能效果已然不同了
说明
1、只要有 yield 关键字，那么虽然看上去是调函数，实际上已经创建了一个生成器对象
2、通过 next() 调用 生成器，可以让这个带有 yield 的 def 代码块，开始执行
  a. 如果是第一次执行，则从 def 代码块的开始部分执行，直到遇到 yield 为止，
     并且把 yield 关键字的数值返回，当作next()的返回值
  b. 如果不是第一次执行，则从上一次暂停的位置（即yield 关键字的下一条语句开始执行），直到遇到下一次 yield 为止，
     并且把 yield 关键字的数值返回，当作 next() 的返回值
"""