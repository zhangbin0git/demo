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

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

