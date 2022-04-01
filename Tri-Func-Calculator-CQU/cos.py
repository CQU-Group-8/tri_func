##########
# 项目名称：Tri-Func-Calculator-CQU
# 最终版本：Tri-Func-Calculator-CQU
# 修订时间：2022年4月1日
# 小组成员：林康志、杜建建、钟豪、朱思宁、戚俊
# 程序说明: 定义COS函数。
##########

from math import pi

def cos(x):
    """
    :param x: 输入参数为角度值
    :return: x的余弦值
    """
    return round(taylor(x, 50), 10)

def factorial(a):    # 阶乘
    b = 1
    while a != 1:
        b *= a
        a -= 1
    return b

def taylor(x, n):
    a = 1
    x = x/180 * pi    # 转换为弧度
    count = 1
    for k in range(1, n):
        if count % 2 != 0:
            a -= (x**(2*k))/factorial(2*k)
        else:
            a += (x**(2*k))/factorial(2*k)
        count += 1
    return a
