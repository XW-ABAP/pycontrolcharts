import pandas as pd
from pycontrolcharts import calc_p, ChartType
from pycontrolcharts.plotting import plot_control_chart

# 模拟数据：人为制造几个失控点（例如第 3 个和第 7 个不合格数非常高）
defect_counts = [3, 2, 15, 1, 5, 2, 18, 2, 1, 4]  # 调大了第 3 和第 7 个元素
sample_sizes = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

# 1. 计算 P 控制图数据
df_result = calc_p(data=defect_counts, sample_size=sample_sizes)

# 2. 打印计算后的 DataFrame 结果
print("--- SPC P图 计算结果 ---")
print(df_result[['point_id', 'value', 'center_line', 'ucl', 'lcl', 'violations']].to_string())

# 3. 筛选出失控点
violations_df = df_result[df_result['violations'].apply(len) > 0]
print(f"\n发现的失控点数量: {len(violations_df)}")
print(violations_df[['point_id', 'value', 'center_line', 'ucl', 'lcl', 'violations']])

# 4. 绘制 Plotly 交互式 P 图
fig = plot_control_chart(
    df_result, 
    chart_type=ChartType.P, 
    title="P 控制图 (包含异常点测试)"
)
fig.show()