# pandas 문제 3)  타이타닉 승객 데이터를 사용하여 아래의 물음에 답하시오.
# 1) 데이터프레임의 자료로 나이대(소년, 청년, 장년, 노년)에 대한 생존자수를 계산한다.
# cut() 함수 사용
#      bins = [1, 20, 35, 60, 150]
#      labels = ["소년", "청년", "장년", "노년"]
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')
# print(df)

df = pd.DataFrame(df)
print(df)
bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
df.age = pd.cut(df.age,bins,labels = labels)
print(df.age)


'''
human_df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/human.csv')
print(human_df.head(2))
print(human_df.info())

human_df = human_df.rename(columns=lambda x: x.strip())
human_df['Group'] = human_df['Group'].str.strip()
human_df = human_df[human_df['Group']!='NA']
print(human_df.head(5),"\n")
'''