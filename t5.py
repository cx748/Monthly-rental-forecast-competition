#coding=gbk
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

#ʹ�ö�Ԫ���Իع���Ԥ��
def regression_model(reg,train_data,train_y,val_data,val_y,input_feature):
    reg.fit(train_data.as_matrix(columns=input_feature),train_y)
    predict_y=reg.predict(val_data.as_matrix(columns=input_feature))
    RMSE=mean_squared_error(val_y,predict_y)**0.5
    return reg,RMSE,predict_y

if __name__=='__main__':
    #��ȡѵ��������֤��
    train_data=pd.read_pickle('train_data.pickle')
    val_data=pd.read_pickle('val_data.pickle')
    train_y=pd.read_pickle('train_y.pickle')
    val_y=pd.read_pickle('val_y.pickle')

    # #ʹ�ö�Ԫ���Իع飬ѡ�������Ա�����Ԥ��,RMSEΪ4.2963
    # reg=LinearRegression()
    # reg,RMSE,predict_y=regression_model(reg,train_data,train_y,val_data,val_y,train_data.columns)
    # print('RMSE for all features with multiple regression: %s'%RMSE)

    #ʹ�����ɭ�ֽ���������ȡ
    np.random.seed(21)
    rf_reg=RandomForestRegressor(n_estimators=50,verbose=1)
    rf_reg.fit(train_data,train_y)
    combine_lists=lambda item: [item[0],item[1]]
    feature_importance=list(map(combine_lists,zip(train_data.columns,rf_reg.feature_importances_)))
    feature_importance=pd.DataFrame(
        feature_importance,columns=['feature','importance']
    ).sort_values(by='importance',ascending=False)
    #����������Ҫ�ԵĽ��
    feature_importance.to_csv('feature_importance_using_randomForest.csv',sep=',',encoding='gbk')
    #���˵���Ҫ��С��0.001����������
    filter_feature=feature_importance[feature_importance['importance']>0.0000187]['feature']
    filter_feature.to_pickle('filter_feature_top250.pickle')



