# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：01-通过修改列表推导式创建生成器.py
@Author  ：DearMCgood
@Date    ：2022/5/6 11:14 
"""

"""
@生成器 generator
简单来说：如果需要很多数据的列表，我们可以有2种方案
方案1: 一次性全部生成（可以使用列表）
      优先：简单、明了
      缺点：占用大量的内存空间
方案2: 什么时候要什么时候生成（生成器）
      优点：不需要大量的空间事先存储数据，减少内存的浪费
      缺点：麻烦，不太容易理解

什么是生成器？只记录生成数据的方法（算法），而不是 事先生成 存储 这些数据，这种方式称之为 “生成器” “边用边生成”
应用点：
如果需要的数据很少，例如10个、20个等，此时我们为了更快的生成这些数据，可以直接使用 列表 或者 列表生成式
而如果需要的数据个数 不确定，推荐使用 生成器

生成器是一种特殊的迭代器
"""

# 创建生成器的 方法1
# 只需要把一个列表生成式的 [ ] 改为 ( )
nums = [x for x in range(5)]  # 列表生成式
print(type(nums))
print(nums)

# >>> <class 'list'>
# >>> [0, 1, 2, 3, 4]

nums = (x for x in range(5))  # 生成器
print(type(nums))
print(nums)

# >>> <class 'generator'>
# >>> <generator object <genexpr> at 0x10ba2a150>

# 对比区别：
# 卡住了，先生成在输出，内存cpu在上升
nums = [x for x in range(500000000000000)]
for num in nums:
    print(num)

# 直接出结果 "边用边生成"
nums = (x for x in range(500000000000000))
for num in nums:
    print(num)

