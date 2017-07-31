#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-7-29 上午1:34
# @Author  : Zhangbin
# @Site    : home
# @File    : survey.py
# @Software: PyCharm Community Edition
# 匿名调查类
class AnonymousSurvey():
    """收集匿名调查的问卷"""
    def __init__(self, question):
        """储存一个问题，并为储存答案做好准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """储存单份问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print("- " + response)