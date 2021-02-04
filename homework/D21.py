import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset('titanic')
sns.barplot(data=df, x='sex', y='survived', hue='class')
survived = df.groupby(['pclass', 'sex']).survived.sum()
plt.figure()
survived.plot(kind='bar')
survived_count = pd.crosstab([df.pclass, df.sex], df.survived)

survived_count.plot(kind='bar', stacked=True)
plt.figure()
sns.violinplot(data=survived_count)
g = sns.FacetGrid(data=df, col='survived')
g.map(plt.hist, 'sex')
h = sns.FacetGrid(data=df, col='survived')
h.map(plt.hist, 'pclass')

plt.show()
