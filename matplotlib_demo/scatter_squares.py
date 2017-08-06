#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 上午9:53
# @Author  : Zhangbin
# @Site    : home
# @File    : scatter_squares.py
# @Software: PyCharm Community Edition
# 绘制1000个散点
import matplotlib.pyplot as plt
# 指定x，y的值
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# x_values = [100]
# y_values = [100 ** 3]
# 绘制散点,其中的S是散点的大小,edgecolor表示边框线，c表示颜色，cmap表示渐变颜色
plt.scatter(x_values, y_values, s=100, edgecolor='none', c=y_values,
            cmap=plt.cm.Blues)
# 设置图标标题并给坐标轴加上标签
# 设置图标标题
plt.title("Squares Numbers", fontsize=24)
# 设置x轴标题
plt.xlabel("Value", fontsize=24)
# 设置y轴标题
plt.ylabel("Squares of Value", fontsize=24)
# 设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=14)
# 设置坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
# 自动保存图表
plt.savefig("squares_plot.png", bbox_inches='tight')
# 绘制数表
plt.show()