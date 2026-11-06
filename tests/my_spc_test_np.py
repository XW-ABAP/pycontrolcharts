import pandas as pd
from pycontrolcharts import ChartType, calc_np
from pycontrolcharts.plotting import plot_control_chart

# 模拟数据：np 图要求样本容量固定（这里设为 100），并包含人为制造的失控点
defect_counts = [3, 2, 15, 1, 5, 2, 18, 2, 1, 4]
sample_size = 100

# 1. 计算 np 控制图数据
df_result = calc_np(data=defect_counts, sample_size=sample_size)

# 2. 打印计算后的 DataFrame 结果
print("--- SPC np图 计算结果 ---")
print(
    df_result[
        ['point_id', 'value', 'center_line', 'ucl', 'lcl', 'violations']
    ].to_string()
)

# 3. 筛选出失控点
violations_df = df_result[df_result['violations'].apply(len) > 0]
print(f"\n发现的失控点数量: {len(violations_df)}")
print(
    violations_df[
        ['point_id', 'value', 'center_line', 'ucl', 'lcl', 'violations']
    ]
)

# 4. 绘制 Plotly 交互式 np 图
fig = plot_control_chart(
    df_result, chart_type=ChartType.NP, title="np 控制图 (包含异常点测试)"
)
fig.show()