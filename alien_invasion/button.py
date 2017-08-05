#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-5 上午8:51
# @Author  : Zhangbin
# @Site    : home
# @File    : button.py
# @Software: PyCharm Community Edition
# 按钮类
import pygame
class Button():
    """PLAY按钮类"""
    #初始化属性
    def __init__(self, screen, msg):
        #所展示的屏幕属性
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #设置按钮的尺寸/颜色/字体
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        #设置字体
        self.font = pygame.font.SysFont(None, 48)
        #创建按钮的rect,并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 按钮的标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将text渲染为图像，并居中"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #绘制button
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)