# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：cloudera_manager_mon.py
@Author  ：DearMCgood
@Date    ：2022/5/20 17:35 
"""


class HttpMon(object):

    def __init__(self:
        self.timestamp = time.time()
        self.webserver = "http://172.18.10.121:19000/opentsdb/put"
        self.data_source_url = "http://114.112.36.69:7180/api/v19/hosts"

    def __call__(self, *args, **kwargs):
        self.collect()
        requests.post(url=self.webserver, data=json.dumps(self.data))

    def record(self, metric, module, ip, value):
        ret = {
            "metric": metric,
            "timestamp": int(self.timestamp),
            "tags": {
                "ident": "Cloudera_Manager",
                "module": str(module),
                "host": str(ip)
            },
            "value": value
        }
        return ret