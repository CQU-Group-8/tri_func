##########
# 项目名称：Tri-Func-Calculator-CQU
# 最终版本：Tri-Func-Calculator-CQU
# 修订时间：2022年4月1日
# 小组成员：林康志、杜建建、钟豪、朱思宁、戚俊
# 程序说明: 定义ARCTAN函数。
##########

from math import pi
from math import fabs

def atan(x):
    """
    :param x: 输入参数为数值
    :return: 输出为角度值
    """
    if fabs(x) < 1:      # 输入值绝对值小于1时，采用泰勒级数展开
        g = x
        # t = x
        n = 1
        while n < 9999:
            t = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
            g += t
            n += 1
    else:               # 输入值绝对值大于1，用 pi/2 - atan(x)
        x = 1/x
        g = x
        # t = x
        n = 1
        while n < 9999:
            t = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
            g += t
            n += 1
        g = pi/2 - g
        
    if x >= 0:
        g = round(g / pi * 180, 10)
    
    elif x < 0:
        if g >= 0:
            g = round((g - pi) / pi * 180, 10)
        else:
            g = g + pi
            g = round((g - pi) / pi * 180, 10)
        
    return g
