# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：06-带有参数的装饰器.py
@Author  ：DearMCgood
@Date    ：2022/5/6 10:31 
"""

import time


# 带有参数的装饰器

def call_out2(timeout=0):
    def call_out(func):
        def call():
            print('-----1-----')
            time.sleep(timeout)
            ret = func()
            print('-----2-----')
            return ret

        return call

    return call_out


@call_out2(2)
def print_hello():
    print("hello word")
    return "ok"


@call_out2(3)
def print_word():
    print("hello word 2222")
    return "ok"


print(print_hello())
print(print_word())

# >>> -----1-----
# >>> hello word
# >>> -----2-----
# >>> ok
# >>> -----1-----
# >>> hello word 2222
# >>> -----2-----
# >>> ok
