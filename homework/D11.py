import pandas as pd

q_df = pd.DataFrame([['male', 'teacher'], ['male', 'engineer'], ['female', None], ['female', 'engineer']],columns=['Sex','Profession'])

df = q_df.fillna('others')

pf = pd.get_dummies(df['Profession'])

data = pd.concat([df, pf], axis=1)
print(data)

print('Column Profession is orderless series, used one-hot encoding.')