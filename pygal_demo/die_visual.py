#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-8-6 下午9:03
# @Author  : Zhangbin
# @Site    : home
# @File    : die_visual.py
# @Software: PyCharm Community Edition
# 投掷骰子
import die
import pygal
import webbrowser
def run_die():
    """运行投掷骰子"""
    # 实例话Die
    die1 = die.Die()
    die2 = die.Die(10)
    # 生成两个骰子的组合结果
    tow_results = to_results(die1, die2)
    # 生成两个骰子的频率
    tow_frequencies = to_frequency(tow_results)
    # 生成结果的交集组合，其中没有重复的，并排序
    tow_results_sides = sorted(set(tow_results))
    # 显示图表
    show_die(tow_results_sides, tow_frequencies)
    webbrowser.open_new_tab("http://localhost:63342/Demo/"
                            "pygal_demo/die_visual.svg")



def to_results(die1, die2):
    # 投掷两次骰子，将结果储存在一个列表中
    results = [die1.roll() + die2.roll() for a in range(1000)]
    return results

def to_frequency(results):
    """生成频率"""
    # 分析结果
    # 存储结果
    frequencies = []
    # 计算two面数的组合
    results_set = sorted(set(results))
    # 建立结果值的循环
    for value in results_set:
        # 将每个值的频率存储
        frequency = results.count(value)
        # 存入frequencies
        frequencies.append(frequency)
    return frequencies

# 对结果进行可视化
def show_die(results_sides, frequencies):
    """生成图表展示"""
    hist = pygal.Bar()
    hist.title = "Result of rolling two die 1000 times"
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    hist.x_labels = results_sides
    hist.add("die", frequencies)
    hist.render_to_file("die_visual.svg")

run_die()
