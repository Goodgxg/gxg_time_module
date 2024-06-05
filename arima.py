# @copyright all reseved
# @author: Persist_Zhang
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# 步骤1：导入必要的库

# 步骤2：加载时间序列数据
# 示例数据
date_rng = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
data = pd.DataFrame(date_rng, columns=['date'])
data['value'] = np.random.randn(len(date_rng))

# 步骤3：可视化原始时间序列
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['value'], label='Original Time Series')
plt.title('Original Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# 步骤4：差分操作，使序列平稳
differenced_data = data['value'].diff().dropna()

# 步骤5：确定ARIMA模型的阶数
# 绘制ACF图
plot_acf(differenced_data)
plt.title('Autocorrelation Function (ACF)')
plt.show()

# 绘制PACF图
plot_pacf(differenced_data)
plt.title('Partial Autocorrelation Function (PACF)')
plt.show()

# 步骤6：拟合ARIMA模型
p, d, q = 1, 1, 1  # 根据ACF和PACF的结果设置p和q的值
arima_model = ARIMA(data['value'], order=(p, d, q))
arima_result = arima_model.fit()

# 步骤7：模型诊断
print(arima_result.summary())

# 步骤8：模型预测
forecast_steps = 10
forecast = arima_result.get_forecast(steps=forecast_steps)
forecast_index = pd.date_range(data['date'].iloc[-1], periods=forecast_steps + 1, freq='D')[1:]
forecast_values = forecast.predicted_mean

# 绘制原始数据和预测结果
plt.figure(figsize=(12, 8))
plt.plot(data['date'], data['value'], label='Original Time Series')
plt.plot(forecast_index, forecast_values, color='red', label='ARIMA Forecast')
plt.title('ARIMA Model Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

