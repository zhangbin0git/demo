#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-2 下午9:29
# @Author  : Zhangbin
# @Site    : home
# @File    : alien.py
# @Software: PyCharm Community Edition
# 创建一个外星人的类
import pygame
class Alien(pygame.sprite.Sprite):
    """表示单个外星人的类"""
    def __init__(self, settings, screen):
        """初始化外星人"""
        # 对父类的__init__()处理
        super().__init__()
        self.screen = screen
        self.settings = settings
        # 加载外星人的图像
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        #每个外星人在屏幕的左上角
        self.rect.x = self.rect.width   #外星人图片的宽
        self.rect.y = self.rect.height  #外星人图片的高
        # 储存外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """更新外星人的位置"""
        #向右移动外星人
        self.x += self.settings.alien_speed_factor
        self.rect.x = self.x

    def check_edge(self):
        """检查外星人是否在屏幕的边缘"""
        # 如果在边缘就返回True
        # 获取屏幕的尺寸
        screen_rect = self.screen.get_rect()
        # 如果外星人到达右边缘返回True
        if self.rect.right >= screen_rect.right:
            return True
        # 如果外星人在左边缘，返回True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向左或向右移动外星人"""
        self.x += self.settings.alien_speed_factor * \
                  self.settings.fleet_direction
        self.rect.x = self.x