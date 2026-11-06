import pandas as pd
from pycontrolcharts import calc_u, ChartType
from pycontrolcharts.plotting import plot_control_chart

# 使用参考代码中 USPC p276 的真实数据集（包含可变样本面积）
data = pd.DataFrame(
    {
        'Date': [
            '3.6.1948', '4.6.1948', '5.6.1948', '6.6.1948', '7.6.1948',
            '10.6.1948', '11.6.1948', '12.6.1948', '13.6.1948', '14.6.1948',
            '17.6.1948', '18.6.1948', '19.6.1948', '20.6.1948', '24.6.1948',
            '25.6.1948', '26.6.1948', '27.6.1948',
        ],
        'NofLeaks': [
            14, 4, 5, 13, 6, 2, 4, 11, 8, 10,
            3, 11, 1, 3, 6, 8, 5, 2,
        ],
        'NofRadiators': [
            39, 45, 46, 48, 40, 58, 50, 50, 50, 50,
            32, 50, 33, 50, 50, 50, 50, 50,
        ],
    }
)

# 1. 计算 U 控制图数据
# 必须指定 value_column (缺陷数) 和 area_column (样本面积/检查单元数)
df_result = calc_u(
    data, 
    value_column='NofLeaks', 
    label='Date', 
    area_column='NofRadiators'
)

# 2. 打印计算后的 DataFrame 结果
print("--- SPC U图 计算结果 ---")
print(df_result[['point_id', 'label', 'value', 'center_line', 'ucl', 'lcl', 'violations']].to_string())

# 3. 筛选出包含违规/失控的点
violations_df = df_result[df_result['violations'].apply(len) > 0]
print(f"\发现的失控/违规点数量: {len(violations_df)}")
print(violations_df[['point_id', 'label', 'value', 'center_line', 'ucl', 'lcl', 'violations']])

# 4. 绘制 Plotly 交互式 U 图 (呈现阶梯状限值)
fig = plot_control_chart(
    df_result, 
    chart_type=ChartType.U, 
    title="U 控制图 (USPC p276 单位缺陷数/可变面积测试)"
)
fig.show()

# 如果需要从 Python 侧直接保存 HTML，可取消下面这行的注释
# fig.write_html("spc_u_chart_python_export.html")