#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-7-28 上午1:37
# @Author  : Zhangbin
# @Site    : home
# @File    : get_formatted_name.py
# @Software: PyCharm Community Edition

def get_formatted_name(first_name, last_name, middle=""):
    """格式化名字，总共两个字或三个字，middle为默认的"""
    if middle:
        full_name = first_name + " " + middle + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
