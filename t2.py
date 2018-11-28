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

#���Ƹ��������ķֲ���״ͼ
train.hist(figsize=(20,15),bins=50,grid=False)
plt.show()







