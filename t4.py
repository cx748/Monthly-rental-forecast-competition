#coding=gbk
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

columns = ['ʱ��','С����','С�����ݳ�������','¥��','��¥��','�������'
           ,'���ݳ���#1','���ݳ���#2','���ݳ���#3','���ݳ���#4','���ݳ���#5','���ݳ���#6','���ݳ���#7','���ݳ���#8'
           ,'��������','��������','��������','��','λ��','������·',
           '����վ��','����','�����']
train=pd.read_csv('./train2.csv',names=columns,encoding='gbk')

#��ȱʧ�ġ�������·���͡�����վ�㡱���0����ȱʧ�ġ����롱���1
train=train.fillna({'������·':0,'����վ��':0,'����':1})

#ɾ����С�������ֶ�
train.drop('С����',axis=1,inplace=True)

#ѵ�������ֶ���Ϣ�鿴
#print(train.info())
#print(train.describe())

# #���������ֲ�ͼ
# plt.figure(figsize=(12,6))
# plt.subplot(211)
# plt.title('�����ֲ�ͼ')
# sns.distplot(train['�����'])
# plt.subplot(212)
# plt.scatter(range(train.shape[0]),np.sort(train['�����'].values))
# plt.show()

# #���Ƹ��������ķֲ���״ͼ
# train.hist(figsize=(20,15),bins=50,grid=False)
# plt.show()

#��������
continuous_cols=['С�����ݳ�������','��¥��','�������','��������','��������',
                 '��������','����']
# #��������������������Ƥ��ѷ���ϵ�������ҽ������򣬻���ͼ��
# for col in continuous_cols:
#     sns.jointplot(x=col,y='�����',data=train,alpha=0.3,size=4)
# plt.figure(figsize=(12,6))
# train.corr()['�����'][continuous_cols].sort_values(ascending=False).plot(
#     'barh',figsize=(12,6),title='����������������������'
# )
# plt.show()

#�Է����������one-hot���루dummy���룩�����ݳ����Ѿ�תΪone-hot��ʽ����������
categorial_cols=['ʱ��','¥��','��','λ��','������·','����վ��']
for col in categorial_cols:
    dummies=pd.get_dummies(train[col],drop_first=False)
    dummies=dummies.add_prefix("{}#".format(col))
    train.drop(col,axis=1,inplace=True)
    train=train.join(dummies)
# #�鿴һ�½���dummy�����Ժ�����ݼ����ֶ���Ϣ
#     print(train.info())

#�˴����Խ������ݵĹ�һ���������Ż���

#��8:2�ָ�ѵ��������֤��
from sklearn.cross_validation import train_test_split
np.random.seed(21)
target=train['�����']
train.drop('�����',axis=1,inplace=True)
train_data,val_data,train_y,val_y=train_test_split(
    train,target,train_size=0.8,random_state=21
)

#����ѵ��������֤��
train_data.to_pickle('train_data_all.pickle')
val_data.to_pickle('val_data.pickle')
train_y.to_pickle('train_y_all.pickle')
val_y.to_pickle('val_y.pickle')

print(train_data.columns.size)





