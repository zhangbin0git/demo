#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-4 下午10:54
# @Author  : Zhangbin
# @Site    : home
# @File    : geme_stats.py
# @Software: PyCharm Community Edition
# 跟综游戏的统计信息
class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, settings):
        """初始化统计信息"""
        # 让游戏处于非活动状态
        self.game_active = False
        self.settings = settings
        self.high_score = 0
        self.reset_stats()


    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.shiplift = self.settings.ship_limit
        self.score = 0
        self.level = 1
