#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 上午10:19
# @Author  : Zhangbin
# @Site    : home
# @File    : random_walk.py
# @Software: PyCharm Community Edition
# 一个生成随机漫步的数据的类
import random
class RandomWalk():
    """生成一个随机散步的数据的类"""
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        # 随机漫步的步数,默认值为5000
        self.num_points = num_points
        # 设定存储步伐的x,y列表,从0,0原点出发
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """生成随机步伐"""
        # 不断漫步，直到到达指定的长度
        while len(self.x_values) <= self.num_points:
            # 决定前进的方向，以及前进的距离
            # x轴方向
            x_direction = random.choice([1, -1])
            x_distance = random.choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            # y轴方向
            y_direction = random.choice([1, -1])
            y_distance = random.choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            # 拒绝原地踏步
            if x_step == 0 and y_step ==0:
                continue
            # 计算下一点的x值和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            # 加入步伐列表中
            self.x_values.append(next_x)
            self.y_values.append(next_y)