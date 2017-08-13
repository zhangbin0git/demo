#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-13 上午12:30
# @Author  : Zhangbin
# @Site    : home
# @File    : countries.py
# @Software: PyCharm Community Edition
# 国别码
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """根据国家的名称，返回pygal中两个字母的国别码"""
    for code, name in COUNTRIES.items():
        # 判断国名是否相同
        if name == country_name:
            return code
    # 如果没有指定的国家就返回None
    return None

