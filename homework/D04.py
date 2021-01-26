import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])

pro1 = np.greater(english_score, math_score)
num = 0
for i in pro1:
    if i == True:
        num += 1
print('%d students English score higher than Math score.' %num)

pro2 = np.logical_and(chinese_score>math_score, chinese_score>english_score)
flag = 0
for i in pro2:
    if i == True:
        flag += 1

if flag == len(pro2):
    print('All the students highest score is Chinese!')
else:
    print('Some students Math or English Score higher than Chinese! ')