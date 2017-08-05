#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-7-29 下午1:26
# @Author  : Zhangbin
# @Site    : 
# @File    : ship.py
# @Software: PyCharm Community Edition
# 游戏中的元素角色类
# 飞船类
import pygame
class Ship(pygame.sprite.Sprite):
    """飞船类"""

    def __init__(self, settings, screen):
        """初始化飞船的各个参数"""
        # 初始化父类
        super().__init__()
        # 屏幕参数
        self.screen = screen
        # 整体设置
        self.settings = settings
        # 加载飞船的图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # 把图形设置到屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        # 在飞船的属性center中存储小数
        self.center = float(self.rect.centerx)


    def update(self):
        # 根据移动标志调整飞船的位置,更新centsettingser值,限制飞船在屏幕中
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        # 将移动的数值传递给rect.centerx
        self.rect.centerx = int(self.center)

    def blitme(self):
        """在指定位置绘制图像"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """将飞船居中"""
        self.center = self.screen_rect.centerx



