#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-7-29 上午10:55
# @Author  : Zhangbin
# @Site    : home
# @File    : alien_invasion.py
# @Software: PyCharm Community Edition
# 飞机游戏
import sys
import pygame
# 导入settings类
import settings
# 导入船的类
import ship
# 导入功能函数包
import game_funcitons as gf
import alien
def run_game():
    # 初始化游戏并创建一个屏幕对象
    # 实例化类
    ai_settings = settings.Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一个船的实例
    aship = ship.Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = pygame.sprite.Group()
    # 创建一个用于储存外星人的编组
    aliens = pygame.sprite.Group()
    # 创建一个外星人群
    gf.create_fleet(ai_settings, screen, aliens)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标的实践
        gf.check_events(ai_settings, screen, aship, bullets)
        # 检查键盘输入，调整飞船的位置,此条代码是更新ship的位置数据
        aship.update()
        # 调入子弹更新和删除无用的子弹，此条代码是更新bullet的数量数据
        gf.update_bullets(bullets)
        # 调入屏幕更新和飞船更新函数，每次重画面
        gf.update_screen(ai_settings, screen, aship, bullets, aliens)

run_game()