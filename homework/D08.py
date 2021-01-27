import numpy as np

name_list = ['小明', '小華', '小菁', '小美', '小張', 'John', 'Mark', 'Tom']
sex_list = ['boy', 'boy', 'girl', 'girl', 'boy', 'boy', 'boy', 'boy']
weight_list = [67.5, 75.3, 50.1, 45.5, 80.8, 90.4, 78.4, 70.7]
rank_list = [8, 1, 5, 4, 7, 6, 2, 3]
myopia_list = [True, True, False, False, True, True, False, False]

dt = np.dtype({'names': ('name', 'sex', 'weight', 'rank', 'myopia'), 'formats':('<U5', '<U5', 'f', 'i', '?')})

c = np.zeros(8, dtype=dt)
c['name'] = name_list
c['sex'] = sex_list
c['weight'] = weight_list
c['rank'] = rank_list
c['myopia'] = myopia_list

print(c['weight'].mean())

print(c[c['sex'] == 'boy']['weight'].mean())
print(c[c['sex'] == 'girl']['weight'].mean())
