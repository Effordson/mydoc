# import asyncio
# 添加注释1 1 1
#
# async def hello(name):
#     print("hello", name)
#
# c = hello("weige")
#
# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 将协程对象注册到事件循环中，并执行事件循环对象
# loop.run_until_complete(c)



# # task的使用
# import asyncio
#
# async def hello(name):
#     print("hello", name)
#
# c = hello("xiaopang")
#
# loop = asyncio.get_event_loop()
#
# # 创建一个任务对象
# task = loop.create_task(c)
#
# print(task)
# # 将任务对象注册到事件循环中并执行
# loop.run_until_complete(task)
# print(task)


# # future的使用
# import asyncio
#
# async def hello(name):
#     print("hello", name)
#
# c = hello("xiaopang")
#
# loop = asyncio.get_event_loop()
#
# # 创建一个任务对象
# future = asyncio.ensure_future(c)
#
# print(future)
# # 将任务对象注册到事件循环中并执行
# loop.run_until_complete(future)
# print(future)


# # 绑定回调
# import asyncio
#
# def call_back(future):
#     print("I am callback", future.result())
#
# async def hello(name):
#     print("hello", name)
#     return name
#
# c = hello("xiaopang")
#
# loop = asyncio.get_event_loop()
#
# # 创建一个任务对象
# future = asyncio.ensure_future(c)
#
# # 通过任务对象创建一个回调函数(任务对象就是回调函数的参数)
# future.add_done_callback(call_back)
#
# # 将任务对象注册到事件循环中并执行
# loop.run_until_complete(future)


# # 基于异步
# import time
# import asyncio
#
#
# async def request(url):
#     print("正在下载:", url)
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("下载完成:", url)
#
#
# url_list = [
#     "www.baidu.com",
#     "www.sogou.com",
#     "www.bing.com",
# ]
#
# start = time.time()
#
# # 1. 创建一个协程对象
# # 2. 创建一个事件循环对象
# # 3. 创建任务对象(把协程对象封装进去)
# # 4. 将任务对象注册到事件循环中
# # 5. 执行事件循环
# loop = asyncio.get_event_loop()
# task_list = list()
# for url in url_list:
#     c = request(url)
#
#     task = asyncio.ensure_future(c)
#     task_list.append(task)
#
# # 注册并执行事件循环，但是如果传入的任务是一个列表的话，需要使用asyncio.wait进行修饰
# loop.run_until_complete(asyncio.wait(task_list))
#
# print("执行耗时: ", time.time() - start)


# # 将多任务异步协程应用到爬虫中
# import time
# import asyncio
# import requests
#
#
# async def request(url):
#     print(requests.get(url=url).text)
#
#
# url_list = [
#     "http://127.0.0.1:5000/tiger",
#     "http://127.0.0.1:5000/weige",
#     "http://127.0.0.1:5000/xiaopang",
# ]
#
# start = time.time()
#
# loop = asyncio.get_event_loop()
# task_list = list()
# for url in url_list:
#     c = request(url)
#
#     task = asyncio.ensure_future(c)
#     task_list.append(task)
#
# # 注册并执行事件循环，但是如果传入的任务是一个列表的话，需要使用asyncio.wait进行修饰
# loop.run_until_complete(asyncio.wait(task_list))
#
# print("执行耗时: ", time.time() - start)


# # 使用aiohttp模块将多任务异步协程应用到爬虫中
# import time
# import asyncio
# import aiohttp
#
#
# async def request(url):
#     async with aiohttp.ClientSession() as session:
#         async with await session.get(url=url) as response:
#             page_text = await response.text()
#             return page_text
#
#
# url_list = [
#     "http://127.0.0.1:5000/tiger",
#     "http://127.0.0.1:5000/weige",
#     "http://127.0.0.1:5000/xiaopang",
# ]
#
# start = time.time()
#
# loop = asyncio.get_event_loop()
# task_list = list()
# for url in url_list:
#     c = request(url)
#
#     task = asyncio.ensure_future(c)
#     task_list.append(task)
#
# # 注册并执行事件循环，但是如果传入的任务是一个列表的话，需要使用asyncio.wait进行修饰
# loop.run_until_complete(asyncio.wait(task_list))
#
# print("执行耗时: ", time.time() - start)


# 任务的绑定回调应用到爬虫中(实现数据解析)
import time
import asyncio
import aiohttp


def call_back(task):
    print("I am callback")
    print("在这里实现数据解析", task.result())


async def request(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url) as response:
            page_text = await response.text()  # read() text()
            return page_text


url_list = [
    "http://127.0.0.1:5000/tiger",
    "http://127.0.0.1:5000/weige",
    "http://127.0.0.1:5000/xiaopang",
]

start = time.time()

loop = asyncio.get_event_loop()
task_list = list()
for url in url_list:
    c = request(url)

    task = asyncio.ensure_future(c)
    task.add_done_callback(call_back)
    task_list.append(task)

# 注册并执行事件循环，但是如果传入的任务是一个列表的话，需要使用asyncio.wait进行修饰
loop.run_until_complete(asyncio.wait(task_list))

print("执行耗时: ", time.time() - start)


