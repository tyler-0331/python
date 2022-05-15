# Bagging은 Bootstrap Aggregation의 약자입니다. 
# 배깅은 샘플을 여러 번 뽑아(Bootstrap) 각 모델을 학습시켜 결과물을 집계(Aggregration)하는 방법입니다.
# RandomForestClassifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd

df = pd.read_csv('../testdata/titanic_data.csv')
print(df.head(3), df.shape)   # (891, 12)
print(df.isnull().any())

df = df.dropna(subset=['Pclass','Age','Sex'])    # 관심있는 칼럼만 대상으로 null 행 제거
print(df.shape)

df_x = df[['Pclass','Age','Sex']]
print(df_x.head(3))

# 데이터 가공 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
df_x.loc[:,'Sex'] = LabelEncoder().fit_transform(df_x['Sex'])    # 사전 순으로 라벨링 ex) female 이 0 이되고 male이 1이 된다.
# df_x['Sex'] = df_x['Sex'].apply(lambda x: 1 if x == 'male' else 0) 
print(df_x.head(3))

"""
import numpy as np
df_x2 = pd.DataFrame(OneHotEncoder().fit_transform(df_x['Pclass'].values[:,np.newaxis]).toarray(),
                                                   columns = ['f_class','s_class','t_class'],
                                                   index = df_x.index)
print(df_x2.head())
df_x = pd.concat([df_x,df_x2], axis = 1)
print(df_x.head())
"""
df_y = df['Survived']
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# model : RandomForestClassifier - 여러 개의 DecisionTree를 배깅방식으로 처리해 최적화된 앙상블 모델을 구현 
model = RandomForestClassifier(criterion = 'entropy', n_estimators =500)
model = model.fit(x_train, y_train)

import numpy as np
pred = model.predict(x_test)
print('예측값: ', pred[:10])
print('실제값: ', np.array(y_test[:10]))
print('accuracy: ', sum(y_test == pred)/len(y_test))
from sklearn.metrics import accuracy_score
print('accuracy: ', accuracy_score(y_test, pred))

# 교차검증 (cross validation - K-fold)
cross_vali = cross_val_score(model, x_train, y_train, cv = 5)
print(cross_vali)
print(np.round(np.mean(cross_vali),3))  # 5겹 교차검증 처리 모델 평균 정확도 

cross_vali2 = cross_val_score(model, df_x, df_y, cv = 5)
print(cross_vali2)
print(np.round(np.mean(cross_vali2),3))

print()
# 즁요한 변수 확인
import matplotlib.pyplot as plt
print('특성(변수) 중요도 :\n{}'.format(model.feature_importances_))

def plot_feature_importances_func(model):
    n_features = df_x.shape[1]
    plt.barh(range(n_features),model.feature_importances_, align = 'center' )
    plt.yticks(np.arange(n_features), df_x.columns)
    plt.xlabel('attr importances')
    plt.ylabel('attr')
    plt.show()
    
plot_feature_importances_func(model)   

















