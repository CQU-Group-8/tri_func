##########
# 项目名称：Tri-Func-Calculator-CQU
# 最终版本：Tri-Func-Calculator-CQU
# 修订时间：2022年4月1日
# 小组成员：林康志、杜建建、钟豪、朱思宁、戚俊
# 程序说明: 定义ARCSIN函数。
##########

from math import fabs
from math import pi
from calculator_ui.constants import MATH_ERROR

def asin(x):
    """
    :param x: 输入参数为数值
    :return: 输出为角度值或抛出异常
    """

    if -1 <= x <= 1:  # 判断输入数值是否在定义域内
        g = x
        t = x
        n = 1
        while fabs(t) >= 1e-9:  # 采用泰勒级数展开进行计算逼近函数值
            t = t * (2 * n - 1) * (2 * n - 1) * x * x / ((2 * n) * (2 * n + 1))
            n += 1
            g += t
        g = round(g / pi * 180, 10)
        return g
    else:
        # 实现异常处理，当输入超出定义域范围，返回异常error
        return MATH_ERROR
