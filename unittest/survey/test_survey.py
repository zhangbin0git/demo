#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-7-29 上午1:43
# @Author  : Zhangbin
# @Site    : home
# @File    : test_survey.py
# @Software: PyCharm Community Edition
# 测试survry类
import unittest
import survey

# 测试类开始
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey的测试"""
    def test_store_sigle_response(self):
        """测试单个答案会被妥善保存"""
        question = "Who is your name?"
        # 定义实例对象
        my_survey = survey.AnonymousSurvey(question)
        # 存入一个答案
        my_survey.store_response("Zhang Bin")
        # 比较答案
        self.assertIn("Zhang Bin", my_survey.responses)
    def test_store_three_responses(self):
        """测试三个答案"""
        question = "Who is your name?"
        #定义一个实例对象
        my_survey = survey.AnonymousSurvey(question)
        #填入三个答案
        responses = ['Zhang Bin', 'Li Jian Ting', 'Duo Duo']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

#运行主程序
unittest.main()
