#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-7-29 下午12:59
# @Author  : Zhangbin
# @Site    : home
# @File    : settings.py
# @Software: PyCharm Community Edition
# 包含Settings类
class Settings():
    """存储游戏-外星人入侵的所有的类"""
    def __init__(self):
        #初始化游戏的设置
        # 屏幕设置
        # 屏幕的宽/高
        self.screen_width = 1200
        self.screen_height = 500
        # 屏幕的背景颜色
        self.bg_color = (230, 230, 230)
        # 飞船的速度设置
        self.ship_speed_factor = 1.5
        # 设置了子弹的参数
        # 子弹的速度
        self.bulle_speed_factor = 2
        # 子弹的宽度
        self.bullet_width = 3
        # 子弹的高度
        self.bullet_height =15
        # 子弹的颜色
        self.bullet_color = (60, 60, 60)

