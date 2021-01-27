import pandas as pd

data = pd.read_csv('boston.csv', usecols=['CHAS', 'NOX', 'RM'])

data.to_excel('boston.xlsx')