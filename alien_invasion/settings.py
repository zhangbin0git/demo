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
        #初始化游戏的静态设置
        # 屏幕设置
        # 屏幕的宽/高
        self.screen_width = 1200
        self.screen_height = 500
        # 屏幕的背景颜色
        self.bg_color = (230, 230, 230)
        # 子弹的宽度
        self.bullet_width = 1200
        # 子弹的高度
        self.bullet_height =15
        # 子弹的颜色
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        # 外星人下移的速度
        self.fleet_drop_speed = 10
        #ship的life的limit
        self.ship_limit = 3
        #以什么样的节奏加快游戏的速度
        self.speedup_scale = 2
        # 外星人的点出提高速率
        self.score_scale = 1.5
        #初始化动态参数
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化对游戏的进行而变化的参数"""
        # 控制外星人速度,外星人的设置
        self.alien_speed_factor = 1
        # 飞船的速度设置
        self.ship_speed_factor = 1
        # 设置了子弹的参数
        # 子弹的速度
        self.bulle_speed_factor = 4
        # fleet_driection为1时表示向右，-1时表示向左
        self.fleet_direction = 1
        # 设定每击落一个外星人的得分
        self.alien_point = 50

    def increase_speed(self):
        """提高游戏的速度"""
        # 提高外星人速度,外星人的设置
        self.alien_speed_factor *= self.speedup_scale
        # 提高飞船的速度设置
        self.ship_speed_factor *= self.speedup_scale
        # 提高子弹的速度
        self.bulle_speed_factor *= self.speedup_scale
        # 提高高等级的分数
        self.alien_point = int(self.alien_point * self.score_scale)




