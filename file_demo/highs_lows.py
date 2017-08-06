#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午11:07
# @Author  : Zhangbin
# @Site    : home
# @File    : highs_lows.py
# @Software: PyCharm Community Edition
# 总结最高，最低气温
import csv
filename = 'file/sitka_weather_07-2014.csv'
with open(filename, 'r') as out_file:
    reader = csv.reader(out_file)
    for header_row in reader:
        print(header_row)