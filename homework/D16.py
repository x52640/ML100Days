import pandas as pd
import numpy as np

index = pd.date_range("1/1/2019", periods=20, freq='D')
series = pd.Series(range(20), index=index)

for i in series.index:
    print(i, ' ', i.weekday())

print(series.resample('W').mean())