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
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import  GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn import neighbors
import xgboost as xgb
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

#ʹ�ûع���Ԥ��
def regression_model(reg,train_data,train_y,val_data,val_y,input_feature):
    reg.fit(train_data.as_matrix(columns=input_feature),train_y)
    predict_y=reg.predict(val_data.as_matrix(columns=input_feature))
    RMSE=mean_squared_error(val_y,predict_y)**0.5
    return reg,RMSE,predict_y

if __name__=='__main__':
    # ��ȡѵ��������֤��
    train_data = pd.read_pickle('train_data.pickle')
    val_data = pd.read_pickle('val_data.pickle')
    train_y = pd.read_pickle('train_y.pickle')
    val_y = pd.read_pickle('val_y.pickle')
    #��ȡ����ѡ��������,filter_feature������һ��array
    filter_feature=pd.read_pickle('filter_feature.pickle')
    filter_feature = filter_feature.tolist()

    np.random.seed(21)
    # #ʹ����ع�
    # ridge=Ridge()
    # ridge,RMSE,predict_y_ridge=regression_model(ridge,train_data,train_y,val_data,val_y,filter_feature)
    # print('RMSE for ridge_regression: %s'%RMSE)
    # #ʹ��svm�ع�
    # svr=svm.SVR()
    # svr,RMSE,predict_y_svm=regression_model(svr, train_data, train_y, val_data, val_y, filter_feature)
    # print('RMSE for SVM_regression: %s' % RMSE)
    # #ʹ��knn�ع�
    # knn = neighbors.KNeighborsRegressor()
    # knn, RMSE, predict_y_knn = regression_model(knn, train_data, train_y, val_data, val_y, filter_feature)
    # print('RMSE for KNN_regression: %s' % RMSE)
    # #ʹ�þ������ع�
    # dt_gre=DecisionTreeRegressor()
    # dt_gre, RMSE, predict_y_dt = regression_model(dt_gre, train_data, train_y, val_data, val_y, filter_feature)
    # print('RMSE for DecisionTree_regression: %s' % RMSE)

    #���ɷ���
    # #ʹ�����ɭ�ֻع�
    # rf_gre=RandomForestRegressor(n_estimators=100)#�����������,n_estimators��ʾ�������ĸ�����100-200Ϊ��.������������max_features=2, min_samples_split=4, min_samples_leaf=2
    # rf_gre, RMSE, predict_y_rf = regression_model(rf_gre, train_data, train_y, val_data, val_y, filter_feature)
    # print('RMSE for RandomForest_regression: %s' % RMSE)
    # #ʹ��GBRT�ع�
    # gbrt = GradientBoostingRegressor(n_estimators=100)#�����л�����learning_rate=0.1, max_depth=1, random_state=0, loss='quantile'
    # gbrt, RMSE, predict_y_gbrt = regression_model(gbrt, train_data, train_y, val_data, val_y, filter_feature)
    # print('RMSE for GBRT_regression: %s' % RMSE)
    # #ʹ��Adaboost�ع飬���ھ���������
    # ada_tree_backing = DecisionTreeRegressor()
    # ada =AdaBoostRegressor(ada_tree_backing,n_estimators=100,learning_rate=0.001, loss='square')
    # ada, RMSE, predict_y_ada = regression_model(ada, train_data, train_y, val_data, val_y, filter_feature)
    # print('RMSE for Adaboost_regression: %s' % RMSE)
    #ʹ��XGBoost�ع�,XGBoost���ٶȻ��֮ǰ�ļ��ɷ�����ܶࡣlearning_rate �� 0.1 ���С��tree_depth �� 2��8��
    #���Ե��ĳ�������ϣ����ĸ����ʹ�С (n_estimators and max_depth)��ѧϰ�ʺ����ĸ��� (learning_rate and n_estimators)�����е� subsampling rates (subsample, colsample_bytree and colsample_bylevel)
    xgbo=xgb.XGBRegressor(max_depth=20,learning_rate=0.2, n_estimators=300, silent=False, objective='reg:gamma')
    xgbo, RMSE, predict_y_xgbo = regression_model(xgbo, train_data, train_y, val_data, val_y, filter_feature)
    print('RMSE for XGBoost_regression: %s' % RMSE)



    # #�������ɭ�ֵĳ�������Ҳ��������������ģ�͵ĳ�����
    # np.random.seed(21)
    # #��tune_params��������Ҫ΢���Ĳ�����ֵ
    # tune_params={'n_estimators':[50,80,120,150,180,200],
    #             'max_features':['auto','sqrt'],
    #              'max_depth':[50,80,100,120,150]}
    # rf_reg=RandomForestRegressor()#�����п���ָ���������˴�Ϊ��΢���й̶�����Ĳ���
    # grid_search=GridSearchCV(estimator=rf_reg,param_grid=tune_params,verbose=1,n_jobs=-1)
    # grid_search.fit(train_data,train_y)
    # print(grid_search.best_params_)
