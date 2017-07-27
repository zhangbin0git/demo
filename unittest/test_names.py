#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17-7-28 上午1:49
# @Author  : Zhangbin
# @Site    : home
# @File    : test_names.py
# @Software: PyCharm Community Edition
# 单元测试
import unittest
import get_formatted_name
class NamesTestCase(unittest.TestCase):
    """测试get_formatted_name"""
    def test_first_last_name(self):
        """能够正确的处理Zhang Bin这样的名字么"""
        full_name = get_formatted_name.get_formatted_name("zhang", "bin")
        self.assertEqual(full_name, "Zhang Bin")
unittest.main()
