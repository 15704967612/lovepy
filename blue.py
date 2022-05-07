# -*- coding: UTF-8 -*-
"""
@Project ：lovepython 
@File    ：blue.py
@Author  ：DearMCgood
@Date    ：2022/5/7 12:05 
"""
import requests
import json


class BkCmdb(object):
    """
    Tencent Cloud
    Blue Whale Interface
    """

    def __init__(self, *args, **kw):
        self.bk_ip = 'http://172.18.9.218:33032'

        self.headers = {
            'Content-Type': 'application/json',
            'HTTP_BLUEKING_SUPPLIER_ID': '0',
            'BK_USER': 'api',
        }

    @staticmethod
    def to_data(ip, field):
        return json.dumps({
            "page": {
                "start": int(0),
                "limit": int(100),
                "sort": ""
            },
            "pattern": "",
            "bk_biz_id": int(3),
            "ip": {
                "flag": "bk_host_innerip|bk_host_outerip",
                "exact": 1,
                "data": [ip, ]
            },
            "condition": [
                {
                    "bk_obj_id": "host",
                    "fields": [field, ],
                    "condition": []
                },
            ]
        })

    def to_hostname(self, ip):
        url = self.bk_ip + '/api/v3/hosts/search'
        r = requests.post(url, headers=self.headers, data=self.to_data(ip, 'bk_host_name'))
        try:
            return json.loads(r.text)['data']['info'][0]['host']['bk_host_name']
        except IndexError:
            return None


if __name__ == '__main__':
    bk = BkCmdb()
    ret = bk.to_hostname('172.28.5.178')
    print(ret)

