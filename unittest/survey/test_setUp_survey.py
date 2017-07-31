#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-7-29 上午2:03
# @Author  : Zhangbin
# @Site    : home
# @File    : test_setUp_survey.py
# @Software: PyCharm Community Edition
# 使用setUp()方法创造实例
import unittest
import survey
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """创建一次实例和答案，供测试使用"""
        question = "Who is your name?"
        self.my_survey = survey.AnonymousSurvey(question)
        self.responses = ["Zhang Bin", "Li Jian Ting", "Duo Duo"]

    def test_store_single_response(self):
        """测试储存一个答案的"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案的存储"""
        #存储答案
        for response in self.responses:
            self.my_survey.store_response(response)
        #测试三个答案
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
unittest.main()