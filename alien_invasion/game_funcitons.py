#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-7-29 下午4:09
# @Author  : Zhangbin
# @Site    : home
# @File    : game_funcitons.py
# @Software: PyCharm Community Edition
# 包含多个功能性函数
import sys
import pygame
def check_keydown_events(event, ship):
    """相应按下按键"""
    if event.key == pygame.K_RIGHT:
        # 更改向右移动标志，向右移动ship
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动持续的
        ship.moving_left = True

def check_keyup_events(event, ship):
    """相应松开按键"""
    if event.key == pygame.K_RIGHT:
        # 持续向右移动标志False
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 持续向左移动False
        ship.moving_left = False
def check_events(ship):
    """相应按键和鼠标事件"""
    for event in pygame.event.get():
        # 检查鼠标时间
        if event.type == pygame.QUIT:
            sys.exit()
        # 检查键盘事件
        elif event.type == pygame.KEYDOWN:
            # 检查按下，调用按下的函数check_keydown_events
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            # 检查松开，调用松开的函数check_keyup_events
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, aship):
    """更新屏幕，飞船，并切换到最新屏幕"""
    # 每次循环重绘制屏幕,指定了屏幕的颜色
    screen.fill(ai_settings.bg_color)
    # 每次循环指定位置绘制船的图像
    aship.blitme()
    # 让最新的界面可见
    pygame.display.flip()
