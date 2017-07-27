#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-7-28 上午1:39
# @Author  : Zhangbin
# @Site    : home
# @File    : names.py
# @Software: PyCharm Community Edition
# 更加用户的输入格式化名字
import get_formatted_name
print("请输入您的名字，如果退出请输入'q'")
# 循环开始
while True:
    # 输入第一个名字
    first_name = input("请输入firstname")
    if first_name == "q":
        break
    # 输入第二个名字
    last_name = input("请输入lastname")
    if last_name == "q":
        break
    formatted_name = get_formatted_name.get_formatted_name(first_name,
                                                           last_name)
    print("Fullname is " + formatted_name + "!")