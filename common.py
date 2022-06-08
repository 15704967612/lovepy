# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：common.py
@Author  ：DearMCgood
@Date    ：2022/5/6 12:15 
"""
import os
import sys


class Filer(object):

    def __init__(self, file):
        self.file = file
        self.exclude_list = self.reader(os.path.join(os.getcwd(), 'exclude_ip.txt'))
        self.reader_list = self.reader(os.path.join(os.getcwd(), self.file))
        self.diff_list = [line for line in self.reader_list if line not in self.exclude_list]

    @staticmethod
    def reader(file):
        with open(file, 'r') as fd:
            ret = list(set([line.strip() for line in fd.readlines()
                            if not line.strip().startswith('[') and len(str(line.strip())) != 0]))
            return ret

    def writer(self):
        with open(self.file + '.new.hosts', 'a') as fd:
            for line in self.diff_list:
                fd.write(line.strip() + '\n')


if __name__ == '__main__':
    fe = Filer(sys.argv[1])
    fe.writer()


