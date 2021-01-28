import pandas as pd

data1 = pd.read_csv('STOCK_DAY_0050_202009.csv')
data2 = pd.read_csv('STOCK_DAY_0050_202010.csv')

new_data = pd.concat([data1, data2], axis=0, ignore_index=True)

print(new_data[new_data['open'] < new_data['close']])