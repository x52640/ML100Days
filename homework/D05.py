import numpy as np

english_score = np.array([55, 89, 76, 65, 48, 70])
math_score = np.array([60, 85, 60, 68, np.nan, 60])
chinese_score = np.array([65, 90, 82, 72, 66, 77])

e_mean= english_score.mean()
e_max= english_score.max()
e_min= english_score.min()
e_std= english_score.std()

m_mean= np.nanmean(math_score)
m_max= np.nanmax(math_score)
m_min= np.nanmin(math_score)
m_std= np.nanstd(math_score)

c_mean= np.mean(chinese_score)
c_max= np.max(chinese_score)
c_min= np.min(chinese_score)
c_std= np.std(chinese_score)

print('English - Mean:%d, Max:%d, Min:%d, Std:%d' %(e_mean, e_max, e_min, e_std))
print('Math - Mean:%d, Max:%d, Min:%d, Std:%d' %(m_mean, m_max, m_min, m_std))
print('Chinese - Mean:%d, Max:%d, Min:%d, Std:%d' %(c_mean, c_max, c_min, c_std))

math_score[4] = 55
new_m_mean= np.nanmean(math_score)
new_m_max= np.nanmax(math_score)
new_m_min= np.nanmin(math_score)
new_m_std= np.nanstd(math_score)
print('New Math - Mean:%d, Max:%d, Min:%d, Std:%d' %(new_m_mean, new_m_max, new_m_min, new_m_std))


rela = np.corrcoef([english_score, math_score, chinese_score])

print(rela)
print('The highest correlation coefficient with Chinese is English.')