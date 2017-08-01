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
import bullet
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """相应按下按键"""
    if event.key == pygame.K_RIGHT:
        # 更改向右移动标志，向右移动ship
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动持续的
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = bullet.Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """相应松开按键"""
    if event.key == pygame.K_RIGHT:
        # 持续向右移动标志False
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 持续向左移动False
        ship.moving_left = False
def check_events(ai_settings, screen, ship, bullets):
    """相应按键和鼠标事件,检查相应的事件"""
    for event in pygame.event.get():
        # 检查鼠标时间
        if event.type == pygame.QUIT:
            sys.exit()
        # 检查键盘事件
        elif event.type == pygame.KEYDOWN:
            # 检查按下，调用按下的函数check_keydown_events
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            # 检查松开，调用松开的函数check_keyup_events
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕，飞船，并切换到最新屏幕"""
    # 每次循环重绘制屏幕,指定了屏幕的颜色
    screen.fill(ai_settings.bg_color)
    # 每次循环指定位置绘制船的图像
    ship.blitme()
    # 重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 让最新的界面可见
    pygame.display.flip()
