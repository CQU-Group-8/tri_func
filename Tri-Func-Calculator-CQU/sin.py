##########
# 项目名称：Tri-Func-Calculator-CQU
# 最终版本：Tri-Func-Calculator-CQU
# 修订时间：2022年4月1日
# 小组成员：林康志、杜建建、钟豪、朱思宁、戚俊
# 程序说明: 定义SIN函数。
##########

from math import fabs
from math import pi

def sin(x):
    """
    :param x: 输入参数为角度值
    :return: x的正弦值
    """
    x = x / 180 * pi    # 输入角度转换为弧度
    g = 0
    t = x
    n = 1

    # 使用泰勒展开式对sin值进行计算
    while fabs(t) >= 1e-15:   # 设置计算的精度
        g += t
        n += 1
        t = -t * x * x / (2 * n - 1) / (2 * n - 2)
    return round(g, 10)  # 计算结果保留十位小数

# test
ans = sin(60)
print(ans)
