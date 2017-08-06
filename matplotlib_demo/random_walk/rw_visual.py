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
#只要程序处于活动状态，就模拟随机漫步
while True:
    # 创建一个RandomWalk的实例并绘制出来
    rw = random_walk.RandomWalk()
    rw.fill_walk()
    # 设置窗口的大小
    plt.figure(figsize=(10, 2))
    # 设置标题
    plt.title("zhangibn")
    # 绘制线的方式
    # plt.plot(rw.x_values, rw.y_values)
    # plt.show()
    # 绘制点的方式，将点的先后区分开来，通过每个点是1-5000个点的先后顺序
    # cmap是颜色渐变样式，plt.cm.Blues,渐变色数组的len与rw.y_values一致
    num_points_color = list(range(len(rw.y_values)))
    print(len(num_points_color))
    # 绘制随机点
    plt.scatter(rw.x_values, rw.y_values, s=1, edgecolor='none',
                c=num_points_color, cmap=plt.cm.Blues)
    # 绘制起点
    plt.scatter(0, 0, s=600, edgecolor='none', c='green')
    # 绘制终点
    plt.scatter(rw.x_values[-1], rw.y_values[-1], s=200, c='red',
                edgecolor='none')
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    # 检查是否继续循环
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break