#coding=gbk
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

columns = ['ʱ��','С����','С�����ݳ�������','¥��','��¥��','�������','���ݳ���',
           '��ס״̬','��������','��������','��������','���ⷽʽ','��','λ��','������·',
           '����վ��','����','װ�����','�����']
train=pd.read_csv('./train.csv',names=columns,encoding='gbk')
#ԭʼѵ�������ֶ���Ϣ�鿴
print(train.info())

