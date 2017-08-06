#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午8:58
# @Author  : Zhangbin
# @Site    : home
# @File    : die.py
# @Software: PyCharm Community Edition
# 骰子类
import random
class Die():
    """一个骰子的类"""
    def __init__(self, num_sides=6):
        """骰子默认为6个面，和基本的参数"""
        self.num_sides = num_sides

    def roll(self):
        """投掷骰子，等到一个1到骰子面数的数值"""
        return random.randint(1, self.num_sides)
