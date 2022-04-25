##########
# 项目名称：Tri-Func-Calculator-CQU
# 最终版本：Tri-Func-Calculator-CQU
# 修订时间：2022年4月1日
# 小组成员：林康志、杜建建、钟豪、朱思宁、戚俊
# 程序说明: 测试函数。
##########

import unittest
import math
from asin import asin
from acos import acos
from atan import atan
from cos import cos
from sin import sin
from tan import tan


class TestFunc(unittest.TestCase):         # 测试类

    def test_arcsin(self):                 # 测试arcsin函数
        self.assertEqual(math.degrees(math.asin(0)), asin(0))
        self.assertEqual(math.degrees(math.asin(0.7071)), asin(0.7071))
        self.assertEqual(math.degrees(math.asin(0.8660)), asin(0.8660))
        self.assertEqual(math.degrees(math.asin(1)), asin(1))
        self.assertEqual(math.degrees(math.asin(-1)), asin(-1))
        self.assertEqual(math.degrees(math.asin(-0.8660)), asin(-0.8660))

    def test_arccos(self):                  # 测试arccos函数
        self.assertEqual(math.degrees(math.acos(0)), acos(0))
        self.assertEqual(math.degrees(math.acos(0.7071)), acos(0.7071))
        self.assertEqual(math.degrees(math.acos(1)), acos(1))
        self.assertEqual(math.degrees(math.acos(-0.7071)), acos(-0.7071))
        self.assertEqual(math.degrees(math.acos(-1)), acos(-1))
        self.assertEqual(math.degrees(math.acos(-0.8660)), acos(-0.8660))

    def test_arctan(self):                 # 测试arctan函数
        self.assertEqual(math.degrees(math.atan(0)), atan(0))
        self.assertEqual(math.degrees(math.atan(0.5773)), atan(0.5773))
        self.assertEqual(math.degrees(math.atan(1)), atan(1))
        self.assertEqual(math.degrees(math.atan(1.732)), atan(1.732))
        self.assertEqual(math.degrees(math.atan(0)), atan(0))
        self.assertEqual(math.degrees(math.atan(-0.5773)), atan(-0.5773))
        self.assertEqual(math.degrees(math.atan(-1)), atan(-1))
        self.assertEqual(math.degrees(math.atan(-1.732)), atan(-1.732))

    def test_cos(self):                    # 测试cos函数
        self.assertEqual(math.cos(math.radians(30)), cos(30))
        self.assertEqual(math.cos(math.radians(60)), cos(60))
        self.assertEqual(math.cos(math.radians(90)), cos(90))
        self.assertEqual(math.cos(math.radians(120)), cos(120))
        self.assertEqual(math.cos(math.radians(180)), cos(180))


    def test_sin(self):                    # 测试sin函数
        self.assertEqual(math.sin(math.radians(30)), sin(30))
        self.assertEqual(math.sin(math.radians(60)), sin(60))
        self.assertEqual(math.sin(math.radians(90)), sin(90))
        self.assertEqual(math.sin(math.radians(120)), sin(120))
        self.assertEqual(math.sin(math.radians(180)), sin(180))


    def test_tan(self):                     # 测试tan函数
        self.assertEqual(math.tan(math.radians(30)), tan(30))
        self.assertEqual(math.tan(math.radians(60)), tan(60))
        self.assertEqual(math.tan(math.radians(120)), tan(120))
        self.assertEqual(math.tan(math.radians(180)), tan(180))


if __name__ == '__main__':
    unittest.main()

