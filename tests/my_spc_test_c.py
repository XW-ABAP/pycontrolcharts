import pandas as pd
from pycontrolcharts import calc_c, ChartType
from pycontrolcharts.plotting import plot_control_chart

# 使用参考代码中 USPC p220 的真实数据集（包含已知的失控点与趋势）
data = pd.DataFrame(
    {
        'Month': [
            '1-01', '1-02', '1-03', '1-04', '1-05', '1-06',
            '1-07', '1-08', '1-09', '1-10', '1-11', '1-12',
            '2-01', '2-02', '2-03', '2-04', '2-05', '2-06',
            '2-07', '2-08', '2-09', '2-10', '2-11', '2-12',
        ],
        'Number of injuries': [
            6, 2, 4, 8, 5, 4, 23, 7, 3, 5, 12, 7,
            10, 5, 9, 4, 3, 2, 2, 1, 3, 4, 3, 1,
        ],
    }
)

# 1. 计算 C 控制图数据
df_result = calc_c(data, value_column='Number of injuries', label='Month')

# 2. 打印计算后的 DataFrame 结果
print("--- SPC C图 计算结果 ---")
print(df_result[['point_id', 'label', 'value', 'center_line', 'ucl', 'lcl', 'violations']].to_string())

# 3. 筛选出包含违规/失控的点
violations_df = df_result[df_result['violations'].apply(len) > 0]
print(f"\n发现的失控/违规点数量: {len(violations_df)}")
print(violations_df[['point_id', 'label', 'value', 'center_line', 'ucl', 'lcl', 'violations']])

# 4. 绘制 Plotly 交互式 C 图
fig = plot_control_chart(
    df_result, 
    chart_type=ChartType.C, 
    title="C 控制图 (USPC p220 伤害频次测试)"
)
fig.show()

# 如果需要保存为 HTML 文件，可以取消下面这行的注释
# fig.write_html("spc_c_chart.html")