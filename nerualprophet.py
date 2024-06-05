import pandas as pd
from neuralprophet import NeuralProphet, set_log_level

# Load the dataset for tutorial 4 with the extra temperature column
# df = pd.read_csv("https://github.com/ourownstory/neuralprophet-data/raw/main/kaggle-energy/datasets/tutorial01.csv")
# df.head()
# df = pd.DataFrame({'ds': pd.date_range(start = '2022-12-01', periods = 10, freq = 'D'),
#                    'y': [9.59, 8.52, 8.18, 8.07, 7.89, 8.09, 7.84, 7.65, 8.71, 8.09]})
df=pd.read_csv('data/bill_unit_2024.csv',index_col=0,parse_dates=True)

# Disable logging messages unless there is an error
set_log_level("ERROR")

# Default model
m = NeuralProphet()

m.set_plotting_backend("plotly-static")

# Continue training the model and making a prediction
metrics = m.fit(df)
forecast = m.predict(df)
m.plot(forecast)

