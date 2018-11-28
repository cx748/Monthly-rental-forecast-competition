#coding=gbk
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

#ʹ�ûع���Ԥ�⣨��Բ��Լ���
def regression_model(reg,train_data,train_y,test_data,input_feature):
    reg.fit(train_data.as_matrix(columns=input_feature),train_y)
    predict_y=reg.predict(test_data.as_matrix(columns=input_feature))
    return reg,predict_y

if __name__=='__main__':
    #��ȡѵ��������Լ�
    train_data = pd.read_pickle('train_data.pickle')
    train_y = pd.read_pickle('train_y.pickle')
    test_data=pd.read_pickle('test_data.pickle')
    # ��ȡ����ѡ��������
    filter_feature = pd.read_pickle('filter_feature.pickle')
    filter_feature = filter_feature.tolist()

    # # ʹ�����ɭ�ֻع�
    # rf_gre = RandomForestRegressor()
    # rf_gre, predict_y_rf = regression_model(rf_gre, train_data, train_y, test_data, filter_feature)

    #ʹ�õ�������������ɭ�ֻع�
    rf_reg=RandomForestRegressor(n_estimators=40,max_features='auto',max_depth=50)
    rf_reg,predict_y_rf=regression_model(rf_reg,train_data, train_y, test_data, filter_feature)

    #��Ԥ��������
    np.savetxt('predict_result.txt',predict_y_rf)


