# import numpy as np
# import pandas as pd
# from statsmodels.tsa.vector_ar.var_model import VAR
#
#
# # 假设你有一个pandas DataFrame 'df'，其中包含多个时间序列列
# # 这里的代码只是为了演示，你需要用自己的数据替换'df'
# # 例如: df = pd.read_csv('your_data.csv')
#
# # 示例数据：创建两个随机的时间序列
# np.random.seed(1)
# n_samples = 100
# x1 = np.random.randn(n_samples)
# x2 = 0.5 * x1[:-1] + np.random.randn(n_samples - 1)  # x2稍微依赖于x1
# x2 = np.insert(x2, 0, 0)  # 为了保持相同的长度，在x2的开头插入一个0
#
# # 将数据放入DataFrame
# df = pd.DataFrame({'x1': x1, 'x2': x2})
#
# # 拟合VAR模型，假设我们想要一个2阶的VAR模型
# model = VAR(df)
#
# # 估计模型参数
# results = model.fit()
#
# # 输出摘要信息
# print(results.summary())
#
# # 预测（需要未来的输入或假设未来的输入保持不变）
# # 在这个例子中，我们只是预测接下来的5个时期，假设未来的输入与最后一个观察值相同
# y = df.values[:]  # 使用最后几个观察值作为初始值
# y_forecasted = results.forecast(y, steps=5)
#
# # 输出预测结果
# print(y_forecasted)


import numpy as np
import pandas as pd
import statsmodels.api as sm


data_pm=pd.read_csv('data/bill_unit_2024.csv',index_col=0,parse_dates=True)

module = sm.tsa.VAR(data_pm)
results = module.fit(2)
print(results.summary())
pred = results.forecast(data_pm.values[-2:],100)
pred
