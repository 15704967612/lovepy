# -*- coding: UTF-8 -*-
"""
@Project ：lovepython 
@File    ：cat.py.py
@Author  ：DearMCgood
@Date    ：2022/5/7 00:01 
"""
import time
import re
import requests

from bs4 import BeautifulSoup


class Cat(object):
    """
    @获取Cat业务分组信息
    """

    def __init__(self, ip):
        self.ip = "http://%s:8197/cat/r/t" % ip
        self.service_ip_list = self.__obtain_service_map()

    def __obtain_service_args(self):
        r = requests.get(self.ip + '?domain=cat&ip=&date=%s&reportType=day&op=view'
                         % time.strftime("%Y%m%d%H", time.localtime()))
        bs = BeautifulSoup(r.text, 'html.parser')
        r.close()
        return [str(ret['href']) for ret in bs.find_all('a', class_="domainItem")]

    def __obtain_service_map(self):
        __service_map_list = []
        for url in self.__obtain_service_args():
            domain = re.search('^\?op=view&domain=(?P<domain>.*)&.*&', url).group('domain')
            dit = {domain: []}
            r = requests.get(self.ip + url)
            bs = BeautifulSoup(r.text, 'html.parser')
            r.close()
            ret = bs.find_all('table', class_="machines")
            for _ret in ret:
                for ip in _ret.findAll('a'):
                    if str(ip.string) != "All":
                        dit[domain].append(ip.string)
            __service_map_list.append(dit)
        return __service_map_list


if __name__ == '__main__':
    c = Cat('172.18.25.114')
    ret = c.service_ip_list

    from blue import BkCmdb

    bk = BkCmdb()

    with open('./cat.log', 'a') as fp:
        for _t in ret:
            domain = list(_t.keys())[0]
            fp.write('*' * 80 + '\n')
            fp.write('[%s]\n' % domain)
            for ip in _t[domain]:
                hostname = bk.to_hostname(ip)
                fp.write("%-30s%-20s\n" % (ip, hostname))
