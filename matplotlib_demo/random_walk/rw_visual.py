#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 上午10:45
# @Author  : Zhangbin
# @Site    : home
# @File    : rw_visual.py
# @Software: PyCharm Community Edition
# 创建一个RandomWalk类的实例
import matplotlib.pyplot as plt
import random_walk
# 创建一个RandomWalk的实例并绘制出来
rw = random_walk.RandomWalk()
rw.fill_walk()
# 绘制线的方式
# plt.plot(rw.x_values, rw.y_values)
# plt.show()
# 绘制点的方式
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()