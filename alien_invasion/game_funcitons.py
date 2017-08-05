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
import time
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

def check_events(ai_settings, screen, ship, bullets, game_stats,
                 play_button, aliens, score_board):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_stats, play_button, mouse_x, mouse_y,
                              aliens, bullets, ai_settings, screen, ship,
                              score_board)

def check_play_button(game_stats, play_button, mouse_x, mouse_y, aliens,
                      bullets, settings, screen, ship, score_board):
    """在玩家play时，开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not game_stats.game_active:
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置life
        game_stats.reset_stats()
        # 设定为激活状态
        game_stats.game_active = True
        # 重置记分牌,重置飞机的数量
        score_board.prep_score()
        score_board.prep_level()
        score_board.prep_high_score()
        score_board.prep_ships()
        # 清空子弹和外星人
        aliens.empty()
        bullets.empty()
        # 重置游戏的速度
        settings.initialize_dynamic_settings()
        # 创建一群新的外星人
        create_fleet(settings, screen, aliens, ship)
        ship.center_ship()


def update_screen(ai_settings, screen, ship, bullets, aliens,
                  game_stats, play_button, scoreboard):
    """更新屏幕，飞船，外星人的画面，并切换到最新屏幕"""
    # 每次循环重绘制屏幕,指定了屏幕的颜色
    screen.fill(ai_settings.bg_color)
    #绘制计分板
    scoreboard.show_score()
    #如果游戏处于非活动状态，就显示Play button
    if not game_stats.game_active:
        #绘制botton
        play_button.draw_button()
    # 每次循环指定位置绘制船的图像
    ship.blitme()
    # 绘制外星人
    aliens.draw(screen)
    # 重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 让最新的界面可见
    pygame.display.flip()

def update_bullets(settings, screen, aliens, ship, bullets,
                   game_stats, score_board):
    """更新子弹的位置，并删除无用的子弹"""
    # 更新子弹画面
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(settings, screen, aliens, ship, bullets,
                                  game_stats, score_board)

def check_bullet_alien_collisions(settings, screen, aliens, ship, bullets,
                                  game_stats, score_board):
    """相应子弹和外星人的碰撞，当外星人没有了后，删除现有现在并新建外星人"""
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 为每次击落的外星人计分，并更新计分板
    if collisions:
        # 讲collisions中的键值对中的values读出，他的键是子弹，值是多个外星人
        for aliens in collisions.values():
            game_stats.score += settings.alien_point * len(aliens)
            score_board.prep_score()
        #增加计分
        game_stats.score += settings.alien_point
        #更新计分板
        score_board.prep_score()
        check_high_score(game_stats, score_board)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        #提高游戏的speed
        settings.increase_speed()
        # 提高等级
        game_stats.level += 1
        score_board.prep_level()
        #创建一群外星人
        create_fleet(settings, screen, aliens, ship)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 根据限制发生子弹，如果没有达到限制就发射一颗子弹
    if len(bullets) < ai_settings.bullet_allowed:
        #创建新的子弹并加入编组
        new_bullet = bullet.Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens, ship):
    """创建外星人群"""
    # 创建一个外星人
    a_aline = alien.Alien(ai_settings, screen)
    # 计算一行有效的外星人数量
    number_alien_x = get_number_aliens_x(ai_settings, a_aline.rect.width)
    # 计算创建的行数
    number_rows = get_number_rows(ai_settings, a_aline.rect.height,
                                  ship.rect.height)
    # 创建第多行外星人
    for row_number in range(number_rows):               #y方向
        for alien_number in range(number_alien_x):      #x方向
            # 调入函数创建
            create_alien(ai_settings, screen, alien_number, row_number, aliens)


def get_number_aliens_x(settings, alien_width):
    """计算一行外星人的数量"""
    # 计算你可以容纳多少个外星人，外星人的间距为外星人的宽度
    available_space_x = settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(settings, alien_height, ship_height):
    """计算屏幕可以容纳多少行外星人"""
    # 有效的行数
    available_space_y = (settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(settings, screen, alien_number, row_number, aliens):
    """创建一个外星人并将起放在当前行"""
    # 创建外星人
    a_alien = alien.Alien(settings, screen)
    # 外星人的宽度
    a_alien_width = a_alien.rect.width
    a_alien_height = a_alien.rect.height
    a_alien.x = a_alien_width + 2 * a_alien_width * alien_number
    a_alien.y = a_alien_height + 2 * a_alien_height * row_number
    a_alien.rect.x = a_alien.x
    a_alien.rect.y = a_alien.y
    aliens.add(a_alien)

def update_aliens(settings, game_stats, aliens, bullets, screen,
                  ship, score_board):
    """检查是否到达边缘，并更新外星人的位置"""
    check_fleet_edges(aliens, settings)
    aliens.update()
    # 检查ship与aliens的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, game_stats, aliens, bullets, screen,
                 ship, score_board)
    check_aliens_bottom(settings, game_stats, aliens, bullets, screen,
                        ship, score_board)

def change_fleet_direction(settings, aliens):
    """将外星人下移，并改变方向"""
    # test aliens.sprites()___type
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1

def check_fleet_edges(aliens, settings):
    """外星人到达边缘采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(settings, aliens)
            break   #test__研究break怎么用

def ship_hit(settings, game_stats, aliens, bullets, screen, ship, score_board):
    """响应外星人撞到飞船"""
    if game_stats.shiplift > 0:
        # ship的life减去1
        game_stats.shiplift -= 1
        # 更新飞机的数量
        score_board.prep_ships()
        # 清空子弹和外星人
        aliens.empty()
        bullets.empty()
        # 创建一群外星人
        create_fleet(settings, screen, aliens, ship)
        # 居中飞船
        ship.center_ship()
        # 暂停5秒
        time.sleep(1)
    else:
        # 将游戏处于非激活状态
        game_stats.game_active = False
        #显示光标
        pygame.mouse.set_visible(True)

def check_aliens_bottom(settings, game_stats, aliens, bullets, screen,
                        ship, score_board):
    """检查外星人是否到达低端"""
    # 屏幕的尺寸
    screen_rect = screen.get_rect()
    # 对外星人进行循环
    for alien in aliens.sprites():
        # 如果外星人到达低端
        if alien.rect.bottom >= screen_rect.bottom:
            #向飞船撞到一样处理
            ship_hit(settings, game_stats, aliens, bullets, screen,
                     ship, score_board)
            break

def check_high_score(game_stats, scoreboard):
    # 检查是否诞生新的最高得分
    if game_stats.score > game_stats.high_score:
        game_stats.high_score = game_stats.score
        scoreboard.prep_high_score()







