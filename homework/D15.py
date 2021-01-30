import pandas as pd

score_df = pd.DataFrame([[1,50,80,70,'boy',1],[2,60,45,50,'boy',2],[3,98,43,55,'boy',1],[4,70,69,89,'boy',2],[5,56,79,60,'girl',1],[6,60,68,55,'girl',2],[7,45,70,77,'girl',1],[8,55,77,76,'girl',2],[9,25,57,60,'girl',1],[10,88,40,43,'girl',3],[11,25,60,45,'boy',3],[12,80,60,23,'boy',3],[13,20,90,66,'girl',3],[14,50,50,50,'girl',3],[15,89,67,77,'girl',3]],columns=['student_id','math_score','english_score','chinese_score','sex','class'])


print('數學最高分：%d. 最低分：%d' %(score_df['math_score'].max(), score_df['math_score'].min()))
print('英文最高分：%d. 最低分：%d' %(score_df['english_score'].max(), score_df['english_score'].min()))
print('國文最高分：%d. 最低分：%d' %(score_df['chinese_score'].max(), score_df['chinese_score'].min()))
math_by_class = score_df.groupby('class').mean()
print(math_by_class['math_score'].max())
chinese_by_sex = score_df.groupby('sex').mean()
print(chinese_by_sex['chinese_score'].max() - chinese_by_sex['chinese_score'].min())