##########
# 项目名称：Tri-Func-Calculator-CQU
# 最终版本：Tri-Func-Calculator-CQU
# 修订时间：2022年4月1日
# 小组成员：林康志、杜建建、钟豪、朱思宁、戚俊
# 程序说明: 定义TAN函数。
##########

from tri_function.sin import sin
from tri_function.cos import cos
from calculator_ui.constants import MATH_ERROR

def tan(x):
    """
    :param x: 输入参数为角度值
    :return: x的正切值
    """
    if cos(x, self.is_rad) != 0:
        result = sin(x, self.is_rad) / cos(x, self.is_rad)
        return round(result, 10)  # 计算结果保留十位小数
    else:
        # 实现异常处理，当输入超出定义域范围，返回异常error
        return MATH_ERROR
