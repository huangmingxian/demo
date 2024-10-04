import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('docs/car_data.csv')

# 绘制散点图，展示汽车价格与行驶公里数的关系
plt.scatter(data["Kilometer"], data["Price"], color='red')
plt.title('汽车价格与行驶公里数关系图', fontsize=16)
plt.xlabel('行驶公里数')
plt.ylabel('价格（美元）')

# 添加网格
plt.grid(True)

# 显示图表
plt.show()