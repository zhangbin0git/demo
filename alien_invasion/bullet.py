#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-1 上午7:06
# @Author  : Zhangbin
# @Site    : home
# @File    : bullet.py
# @Software: PyCharm Community Edition
# 添加一个子弹的类
import pygame
# 使用的类是pygame.sprite.Sprite
import pygame.sprite

class Bullet(pygame.sprite.Sprite):
    """一个对飞船发射的子弹进行管理"""
    def __init__(self, ai_settings, screen, ship):
        """初始化子弹的参数"""
        # 对父类的__init__处理
        super().__init__()
        # 传入屏幕的参数
        self.screen = screen
        # 在0.0创建一个表示子弹的矩形，并设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet.width,
                                ai_settings.bullet.hight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 储存用于小数的子弹的位置
        self.y = float(self.rect.y)
        # 子弹的颜色和速度
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bulle_speed_factor

