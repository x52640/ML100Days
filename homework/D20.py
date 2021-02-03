import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid', color_codes=True)
rs = np.random.RandomState(0)
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)
fig, axes=plt.subplots(1,2)
sns.distplot(y, color='g', ax=axes[0])
sns.distplot(y, kde=False, rug=True, bins=15, ax=axes[1])

plt.show()