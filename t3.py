#coding=gbk
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def mapping(s):
    if s=="��":
        return 0
    if s=="��":
        return 1
    if s=="��":
        return 2
    if s=="��":
        return 3
    if s=="����":
        return 4
    if s=="����":
        return 5
    if s=="����":
        return 6
    if s=="����":
        return 7

if __name__=='__main__':
    columns = ['ʱ��','С����','С�����ݳ�������','¥��','��¥��','�������','���ݳ���'
               ,'��������','��������','��������','��','λ��','������·',
               '����վ��','����','�����']
    train=pd.read_csv('./train1.csv',names=columns,encoding='gbk')

    arr=train['���ݳ���']
    #��Է��ݳ�����ַ������ݽ��з��࣬�ֳ�8�ࣺ�� �� �� �� ���� ���� ���� ����
    #����������directions��
    directions=np.zeros((arr.size,8))

    for item in range(arr.size):
        str=arr[item]
        x=str.split()
        for i in x:
            index=mapping(i)
            directions[item][index]=1
    np.savetxt('train_1_directions.csv',directions,delimiter=',')


