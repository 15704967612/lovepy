# -*- coding: UTF-8 -*-
"""
@Project ：lovepy
@File    ：mylogger.py
@Author  ：DearMCgood
@Date    ：2022/5/6 09:14 
"""


import logging


class MyLogging(logging.Logger):
    def __init__(self, level=logging.INFO, file=None):
        """
        :param level: 级别
        :param file: 日志文件名称
        """
        super().__init__(level)

        # 设置日志格式
        fmt = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
        formatter = logging.Formatter(fmt)

        # 文件输出渠道
        if file:
            fh = logging.FileHandler(file, encoding="utf-8")
            fh.setFormatter(formatter)
            fh.setLevel(logging.INFO)
            self.addHandler(fh)
        # 控制台渠道
        else:
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            ch.setLevel(logging.DEBUG)
            self.addHandler(ch)


# 直接实例化，后期每个模块调用就不用实例化，导入可以直接使用
# 实例化 file output
logger = MyLogging(file="./my_log.log")
# 实例化 console output
log_print = MyLogging()


if __name__ == '__main__':
    log_print.info("封装好的日志类，console")
    logger.info("封装好的日志类，文件")