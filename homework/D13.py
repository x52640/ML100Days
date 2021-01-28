import pandas as pd

score_df = pd.DataFrame([[1,56,66,70], [2,90,45,34], [3,45,32,55], [4,70,77,89], [5,56,80,70], [6,60,54,55], [7,45,70,79], [8,34,77,76], [9,25,87,60], [10,88,40,43]],columns=['student_id','math_score','english_score','chinese_score'])



id_6_mean = score_df.loc[score_df['student_id'] == 6, ['math_score', 'english_score', 'chinese_score']].mean(axis=1)
print('id 6 平均分數: ', id_6_mean)
all_mean = score_df.loc[ : , 'math_score':'chinese_score'].mean(axis=1)

all_med = all_mean.median()
print('全班平均中位數', all_med)
if float(id_6_mean) > float(all_med):
    print('id 6 高於班上平均分中位數。')
else:
    print('id 6 低於班上平均分中位數。')

new_score = pd.DataFrame(columns=['id', 'math_score', 'english_score', 'chinese_score'])
new_score['id'] = score_df['student_id']
new_score[['math_score', 'english_score', 'chinese_score']] = score_df[['math_score', 'english_score', 'chinese_score']].apply(lambda x: x**(0.5)*10).round()
new_6_score = new_score[new_score['id'] == 6]
print('id 6 新成績如下：')
print(new_6_score)

print('加權後各科平均分：')
print(new_6_score[['math_score', 'english_score', 'chinese_score']].mean())
