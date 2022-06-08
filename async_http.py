# -*- coding: UTF-8 -*-
"""
@Project ：lovepy 
@File    ：async.py
@Author  ：DearMCgood
@Date    ：2022/6/7 16:03 
"""
import aiohttp
import asyncio
import aiofiles
import datetime
import sys


async def logger(*args, **kwagrs):
    if kwagrs['level'] == 'error':
        lines = kwagrs['url'] + ' ' + str(kwagrs['status']) + '\n'
        async with aiofiles.open(urlfile + '.error_log.txt', 'a') as f:
            await f.write(lines)
    elif kwagrs['level'] == 'info':
        lines = kwagrs['url'] + ' ' + str(kwagrs['status']) + ' ' + str(kwagrs['length']) + '\n'
        async with aiofiles.open(urlfile + '.info_log.txt', 'a') as f:
            await f.write(lines)


async def http(session, url):
    async with session.head(url=url) as resp:
        if resp.status != 200:
            await logger(level="error", url=url, status=resp.status)
        else:
            length = resp.headers['Content-Length']
            lengths.append(int(length))
            await logger(level="info", url=url, status=resp.status, length=length)


async def main():
    with open(urlfile) as f:
        urls = f.readlines()

    # 创建一个全局的session连接池
    async with aiohttp.ClientSession() as session:
        # 创建任务列表
        tasks = [asyncio.create_task(http(session, url.strip())) for url in urls]
        # 等待执行结果
        await asyncio.wait(tasks, timeout=None)


if __name__ == '__main__':
    urlfile = sys.argv[1]
    lengths = []
    start = datetime.datetime.now()
    asyncio.run(main())
    sums = 0
    for length in lengths:
        sums += length
    end = datetime.datetime.now()
    print(f"Total KB: {sums / 1024}KB")
    print("Cost Time: %ss" % (end - start).seconds)