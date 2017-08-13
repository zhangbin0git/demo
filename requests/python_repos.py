#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-14 上午12:26
# @Author  : Zhangbin
# @Site    : home
# @File    : python_repos.py
# @Software: PyCharm Community Edition
import requests
# 执行API调用并存储结果
# 访问网址
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# 存储返回结果
result = requests.get(url)
# 打印状态
print("Status code:" + str(result.status_code))
# 存储为列表dict
response_dict = result.json()
# 打印列表的键
print(response_dict.keys())