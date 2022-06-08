# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：es_search.py
@Author  ：DearMCgood
@Date    ：2022/6/6 16:14 
"""
import json
from elasticsearch import Elasticsearch

elastic = Elasticsearch(hosts="http://172.18.1.112:9200")
query_json = json.dumps(
    {
        "_source": ["request_domain", "request_url"],
        "size": 1000000,
        "query": {
            "bool": {
                "must": [
                    {
                        "terms": {
                            "server_addr": [
                                "114.112.78.162",
                                "114.112.78.163"
                            ]
                        }
                    }, {
                        "match": {
                            "response_status": 200
                        }
                    }

                ],
                "must_not": [
                    {
                        "match": {
                            "request_domain": "song.mvbox.cn"
                        }
                    }
                ]
            }
        }
    }
)

maps = {
    "file.m.mvbox.cn": "cos-file-m.mvbox.cn",
    "data.mvbox.cn": "cos-data.mvbox.cn",
    "images.live.51vv.com": "cos-images-live.51vv.com",
    "images.51vv.com": "cos-images.51vv.com",
    "mpres.51vv.com": "cos-mpres.51vv.com",
    "file.51vv.com": "cos-file.51vv.com",
    "im.51vv.com": "cos-im.51vv.com",
    "msgimg.51vv.com": "cos-msgimg.51vv.com"
}


if __name__ == "__main__":
    ret = elastic.search(index='logstash-nginx-access-all-2022.06.07', body=query_json, request_timeout=600)

    data = list(set(['http://' + maps[line['_source']['request_domain']] + line['_source']['request_url']
                     for line in ret['hits']['hits']]))
    print(f"sum={len(data)}")
    with open('./icl_url_200-2022.06.07', 'a') as f:
        for line in data:
            f.write(line+'\n')
