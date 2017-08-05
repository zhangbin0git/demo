#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-5 上午11:09
# @Author  : Zhangbin
# @Site    : home
# @File    : scoreboard.py
# @Software: PyCharm Community Edition
# 记录分数的类
import ship
import pygame
class Scoreboard():
    """显示得分信息的类"""
    def __init__(self, screen, settings, game_stats):
        """初始化显示得分相关的参数，同时显示最高得分和实时得分"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.game_stats = game_stats
        # 显示得分显示的字体和颜色
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # 初始化得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        """将得分转为一张图像"""
        # 将得分锁定到10的倍数
        rounded_score = round(self.game_stats.score, -1)
        # 将得分转化为string
        score_str= "{:,}".format(rounded_score)
        # 转换为图像
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)
        # 将得分放到屏幕的右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top

    def prep_high_score(self):
        """将最高得分变为图像"""
        # 将最高得分锁定为10的倍数
        high_score = round(self.game_stats.high_score, -1)
        # 将得分格式含有千分符
        high_score_str = "{:,}".format(high_score)
        #转换为图像
        self.high_score_image = self.font.render(high_score_str, True,
                                            self.text_color,
                                            self.settings.bg_color)
        # 设置最高分数的显示位置
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.score_rect.top

    def prep_level(self):
        """玩家的等级以图像的形式渲染到界面上。"""
        self.level_image = self.font.render(str(self.game_stats.level), True,
                                            self.text_color,
                                            self.settings.bg_color)
        # 将等级放在得分 下方
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示剩余的船的数量"""
        self.ships = pygame.sprite.Group()
        for ship_number in range(self.game_stats.shiplift):
            aship = ship.Ship(self.settings, self.screen)
            aship.rect.x = 10 + ship_number * aship.rect.width
            aship.rect.y = 10
            self.ships.add(aship)

    def show_score(self):
        """显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.ships.draw(self.screen)