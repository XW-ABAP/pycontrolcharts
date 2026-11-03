from pycontrolcharts import calc_xmr, ChartType
from pycontrolcharts.plotting import plot_control_chart

# 模拟一组工厂车间的测量数据
data = [39, 41, 41, 41, 43, 44, 41, 42, 40, 41, 44, 40]

# 1. 计算 XmR 控制图数据
df = calc_xmr(data)

# 2. 打印核心数据
print("--- SPC 计算结果 ---")
print(df[['value', 'center_line', 'ucl', 'lcl']].to_string())

# 3. 绘制 Plotly 交互式图表
fig = plot_control_chart(df, chart_type=ChartType.XMR, title="车间数据 XmR 控制图")

# 4. 直接在 Jupyter 单元格下方渲染展示图表
fig.show()