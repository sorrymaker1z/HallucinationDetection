import matplotlib.pyplot as plt

# 准备数据
x = [3.53, 4.31, 4.91, 5.15, 5.99]
y = [69.07, 71.77, 73.37, 73.21, 73.56]
NBC = [56, 65.23, 66.7, 68.4, 70.2, 71.3, 71.7, 71.9]
AVG = [50, 56.1, 58.1, 58.3, 61.8, 61.4, 61.6, 62.0]
MAX = [50, 61, 66.4, 68.9, 70.73, 71.84, 72.23, 72.42]

# 绘制第一条折线图
plt.plot(x, y, label='Bayesian sequential analysis', linestyle='--', marker='o')

# 绘制其他折线图，使用不同的标记
x_new = list(range(1, 9))
plt.plot(x_new, NBC,label='NB C', linestyle='--', marker='^', color='blue')  # 三角形标记，蓝色
plt.plot(x_new, AVG, label='AVG', linestyle='--', marker='s', color='green')  # 方形标记，绿色
plt.plot(x_new, MAX, label='MAX', linestyle='--', marker='D', color='red')    # 菱形标记，红色

# 添加图例
plt.legend()

# 添加标题和坐标轴标签
plt.xlabel('The number of documents retrieved')
plt.ylabel("Spearman's RankCC")


# 调整布局以适应标签
plt.tight_layout()

# 显示图表
plt.show()