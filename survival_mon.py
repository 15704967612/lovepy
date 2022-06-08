# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：survival_mon.py
@Author  ：DearMCgood
@Date    ：2022/5/19 15:15 
"""
import json
import re
import requests
import time
import threading


class HttpMon(object):

    def __init__(self, source: list):
        self.data = []
        self.source = source
        self.timestamp = time.time()
        self.url = "http://172.18.10.121:19000/opentsdb/put"

    def __call__(self, *args, **kwargs):
        self.collect()
        requests.post(url=self.url, data=json.dumps(self.data))

    def record(self, module, ip, value, metric="http_code"):
        ret = {
            "metric": metric,
            "timestamp": int(self.timestamp),
            "tags": {
                "ident": "SurvivalDetection",
                "module": str(module),
                "host": str(ip)
            },
            "value": value
        }
        return ret

    def collect(self):
        def get():
            module = tag[0]
            url = tag[1]
            ip = re.search('(?P<ip>\d+\.\d+\.\d+\.\d+)', url).group('ip')
            try:
                r = requests.get(url, timeout=3)
                value = r.status_code
            except requests.exceptions.Timeout:
                value = 0
            self.data.append(self.record(module, ip, value))

        r_res = []

        for tag in self.source:
            t = threading.Thread(target=get, args=())
            t.start()
            r_res.append(t)

        for t in r_res:
            t.join()


if __name__ == '__main__':
    monconf = "/data/monconf/url.txt"
    if not os.path.exists(monconf):
        print(f'{monconf} 不存在')
        sys.exit(1)
    with open(monconf, 'r') as f:
        data_source = [line.strip().split() for line in f.readlines() if
                       not line.strip().startswith("#") and not line.strip() == ""]
    mon = HttpMon(data_source)
    mon()
