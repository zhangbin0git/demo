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
    # 创建一个外星人
    a_aline = alien.Alien(ai_settings, screen)
    # 计算一行有效的外星人数量
    number_alien_x = get_number_aliens_x(ai_settings, a_aline.rect.width)
    #创建第一行外星人
    for alien_number in range(number_alien_x):
        # 调入函数创建
        create_alien(ai_settings, screen, alien_number, aliens)


def get_number_aliens_x(settings, alien_width):
    """计算一行外星人的数量"""
    # 计算你可以容纳多少个外星人，外星人的间距为外星人的宽度
    available_space_x = settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(settings, alien_height, ship_height):
    """计算屏幕可以容纳多少行外星人"""
    # 有效的行数
    available_space_y = (settings.screen.width - \
                        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(settings, screen, alien_number, row_number, aliens):
    """创建一个外星人并将起放在当前行"""
    # 创建外星人
    a_alien = alien.Alien(settings, screen)
    # 外星人的宽度
    a_alien_width = a_alien.rect.width
    a_alien_height = alien.rect.heigh
    a_alien.x = a_alien_width + 2 * a_alien_width * alien_number
    a_alien.y = a_alien_height + 2 * a_alien_height * row_number
    a_alien.rect.x = a_alien.x
    aliens.add(a_alien)