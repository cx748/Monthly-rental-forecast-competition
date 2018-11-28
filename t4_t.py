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
test=pd.read_csv('./test2.csv',names=columns,encoding='gbk')

#��ȱʧ�ġ�������·���͡�����վ�㡱���0����ȱʧ�ġ����롱���1
test=test.fillna({'������·':0,'����վ��':0,'����':1})

#ɾ����С�������ֶ�
test.drop('С����',axis=1,inplace=True)

#�Է����������one-hot���루dummy���룩�����ݳ����Ѿ�תΪone-hot��ʽ����������
categorial_cols=['ʱ��','¥��','��','λ��','������·','����վ��']
for col in categorial_cols:
    dummies=pd.get_dummies(test[col],drop_first=False)
    dummies=dummies.add_prefix("{}#".format(col))
    test.drop(col,axis=1,inplace=True)
    test=test.join(dummies)

test.to_pickle('test_data.pickle')

print(test.columns.size)