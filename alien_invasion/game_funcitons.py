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
import alien
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """相应按下按键"""
    if event.key == pygame.K_RIGHT:
        # 更改向右移动标志，向右移动ship
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动持续的i
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 根据限制发射子弹
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # 退出程序
        print("welcome back!!!")
        sys.exit()

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

def update_screen(ai_settings, screen, ship, bullets, aliens):
    """更新屏幕，飞船，外星人的画面，并切换到最新屏幕"""
    # 每次循环重绘制屏幕,指定了屏幕的颜色
    screen.fill(ai_settings.bg_color)
    # 每次循环指定位置绘制船的图像
    ship.blitme()
    # 绘制外星人
    aliens.draw(screen)
    # 重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 让最新的界面可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并删除无用的子弹"""
    # 更新子弹画面
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
        print(len(bullets))

def fire_bullet(ai_settings, screen, ship, bullets):
    # 根据限制发生子弹，如果没有达到限制就发射一颗子弹
    if len(bullets) < ai_settings.bullet_allowed:
        #创建新的子弹并加入编组
        new_bullet = bullet.Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    #计算你可以容纳多少个外星人，外星人的间距为外星人的宽度
    a_alien = alien.Alien(ai_settings, screen)
    a_alien_width = a_alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * a_alien_width
    number_alien_x = int(available_space_x/(2*a_alien_width))
    #创建第一行外星人
    for alien_number in range(number_alien_x):
        # 常见一个外星人将他加入当前行
        a_alien = alien.Alien(ai_settings, screen)
        a_alien.x = a_alien_width + 2 * a_alien_width * alien_number
        a_alien.rect.x = a_alien.x
        aliens.add(a_alien)