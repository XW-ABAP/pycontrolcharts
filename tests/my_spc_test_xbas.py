import pandas as pd
from pycontrolcharts import calc_xbar_s, ChartType
from pycontrolcharts.plotting import plot_control_chart

# 将多组数据“拍平”成一个一维列表
flat_data = [
    10.2, 10.4, 10.1, 10.3,
    10.5, 10.2, 10.6, 10.4,
    9.8,  10.1, 10.0, 9.9,
    10.3, 10.5, 10.4, 10.6,
    10.1, 10.0, 10.2, 10.1,
    10.4, 10.3, 10.5, 10.4,
    11.5, 11.2, 11.4, 11.3,
    10.0, 10.1, 9.9,  10.0,
    10.2, 10.3, 10.1, 10.2,
    10.1, 10.2, 10.0, 10.1
]

# 1. 传入一维列表和 subgroup_size 计算 Xbar-S 控制图数据
df_result = calc_xbar_s(flat_data, subgroup_size=4)

# 2. 打印计算后的 DataFrame 结果（包含中心线、UCL、LCL、违规记录等）
print("--- SPC Xbar-S 计算结果 ---")
print(df_result[['point_id', 'value', 'center_line', 'ucl', 'lcl', 'violations']].to_string())

# 3. 筛选出触发了异常判异规则（失控）的行
violations_df = df_result[df_result['violations'].apply(len) > 0]
print("\n发现的失控点：")
print(violations_df[['point_id', 'value', 'center_line', 'ucl', 'lcl', 'violations']])

# 4. 使用 plot_control_chart 绘制 Plotly 交互式 Xbar-S 双联图
fig = plot_control_chart(
    df_result, 
    chart_type=ChartType.XBAR_S, 
    title="Xbar-S 控制图 (Subgroup Size = 4)"
)

# 5. 直接在 Jupyter 单元格下方渲染展示图表
fig.show()