#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-12 下午11:54
# @Author  : Zhangbin
# @Site    : home
# @File    : world_population.py
# @Software: Ptest.jsonyCharm Community Edition
# 全球的人口
# 将数据加载到一个列表中
import json
import pygal
import webbrowser
import countries
file_name = "file/population_data.json"
# 打开文件
with open(file_name) as f:

    population_data = json.load(f)
# 打印每个国家2010年的人口
# 创建一个包含人口数量和国别码的一个字典
# code_populations = {}
# for pop_dict in population_data:
#     if pop_dict['Year'] == '2010':
#         # 打印
#         country_name = pop_dict['Country Name']
#         population = int(float(pop_dict['Value']))
#         # 获取两位的国别码
#         code = countries.get_country_code(country_name)
#         if code:
#             code_populations[code] = population
# # 创建地图
# wm = pygal.maps.world.World()
# # 标题
# wm.title = 'World Population in 2010, by Country'
# # add数据
# wm.add('2010', code_populations)
# # 到处文件
# wm.render_to_file('world_population.svg')
# webbrowser.open_new_tab('http://localhost:63342/Demo/file_demo/'
#                         'world_population.svg?_ijt=3pul86a5d4mo9ckho5ja7kd1sq')
# 分组显示
code_populations = {}
for pop_dict in population_data:
    if pop_dict['Year'] == '2010':
        # 打印
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        # 获取两位的国别码
        code = countries.get_country_code(country_name)
        if code:
            code_populations[code] = population

# 将数据分为三组,根据100000000分类
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cd, pops in code_populations.items():
    if pops < 10000000:
        cc_pops_1[cd] = pops
    elif pops < 1000000000:
        cc_pops_2[cd] = pops
    else:
        cc_pops_3[cd] = pops

# 创建地图

wm = pygal.maps.world.World()
print(help(pygal.maps.world.World()))
# 标题
wm.title = 'World Population in 2010, by Country'
# add数据
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
# 到处文件
wm.render_to_file('world_population.svg')
webbrowser.open_new_tab('http://localhost:63342/Demo/file_demo/'
                        'world_population.svg?_ijt=3pul86a5d4mo9ckho5ja7kd1sq')



