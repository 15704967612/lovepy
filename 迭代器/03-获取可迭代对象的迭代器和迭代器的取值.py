# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：03-获取可迭代对象的迭代器和迭代器的取值.py
@Author  ：DearMCgood
@Date    ：2022/5/6 10:50 
"""

# iter() 获取可迭代对象的迭代器
# next() 迭代器取值
nums = [11, 22, 33, 44]  # 可迭代对象 <class 'list'>
nums_iter = iter(nums)   # 获取迭代器 <class 'list_iterator'>
num = next(nums_iter)    # 迭代器取值

num1 = next(nums_iter)
num2 = next(nums_iter)
num3 = next(nums_iter)
num4 = next(nums_iter)
try:
    num5 = next(nums_iter)
except StopIteration:
    pass

# 上面的5个next()取值等价于下面的方式
for num in nums:
    print(num)

while True:
    try:
        num = next(nums_iter)
        print(num)
    except StopIteration:
        break

i = 0
while i < len(nums):
    num = next(nums_iter)
    print(num)
    i += 1

"""
小总结
for 循环的过程可以通过上面的 iter() 和 next() 函数来实现
也就是说：
1. 先调用iter()，将nums当作实参，得到nums这个可迭代对象的迭代器
2. 调用next()，将上一步得到的迭代器，进行取值
3. 将上一步取出来的值 赋值 给num这个变量
4. 执行for循环体中的代码，print(num)
5. 接下来重复执行2/3/4步，当num中的所有数据都获取完之后，会在下一次调用next的时候产生 StopIteration 异常
   只不过for循环中自带了异常处理，当它遇到StopIteration异常额度时候，会自动结束for循环
"""