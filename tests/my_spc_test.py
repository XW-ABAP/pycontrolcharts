# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

from pycontrolcharts import calc_xmr

# 模拟一组工厂车间的测量数据
data = [39, 41, 41, 41, 43, 44, 41, 42, 40, 41, 44, 40]

# 调用 pycontrolcharts 计算 XmR 控制图
df = calc_xmr(data)

# 打印计算结果
print("--- SPC 计算结果 ---")
print(df[['value', 'center_line', 'ucl', 'lcl']])