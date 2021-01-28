import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('boston.csv')

data.boxplot()

data.plot.scatter(x='NOX', y='DIS')

print('TAX and B中位數在300-400之間。')
print('DIS加權越大，表示離商業區越遠，一氧化碳濃度越低。一氧化碳濃度與距離市區遠近是線性關係。')
plt.show()
