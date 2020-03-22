# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 22:20:21 2020

@author: hp
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset_tain=pd.read_csv('train.csv')  
dataset_test=pd.read_csv('test.csv')  

dataset_tain.Alley.astype(str)
dataset_tain.fillna('NA',inplace=True)
dataset_test.Alley.astype(str)
dataset_test.fillna('NA',inplace=True)

#Encoding Categrical Data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
dataset_tain.MSZoning=labelencoder_X.fit_transform(dataset_tain.MSZoning)
dataset_tain.Street=labelencoder_X.fit_transform(dataset_tain.Street)
dataset_tain.LotShape=labelencoder_X.fit_transform(dataset_tain.LotShape)
dataset_tain.LandContour=labelencoder_X.fit_transform(dataset_tain.LandContour)
dataset_tain.Utilities=labelencoder_X.fit_transform(dataset_tain.Utilities)
dataset_tain.LotConfig=labelencoder_X.fit_transform(dataset_tain.LotConfig)
dataset_tain.LandSlope=labelencoder_X.fit_transform(dataset_tain.LandSlope)
dataset_tain.Neighborhood=labelencoder_X.fit_transform(dataset_tain.Neighborhood)
dataset_tain.Condition1=labelencoder_X.fit_transform(dataset_tain.Condition1)
dataset_tain.Condition2=labelencoder_X.fit_transform(dataset_tain.Condition2)
dataset_tain.BldgType=labelencoder_X.fit_transform(dataset_tain.BldgType)
dataset_tain.HouseStyle=labelencoder_X.fit_transform(dataset_tain.HouseStyle)
dataset_tain.RoofStyle=labelencoder_X.fit_transform(dataset_tain.RoofStyle)
dataset_tain.RoofMatl=labelencoder_X.fit_transform(dataset_tain.RoofMatl)
dataset_tain.Exterior1st=labelencoder_X.fit_transform(dataset_tain.Exterior1st)
dataset_tain.Exterior2nd=labelencoder_X.fit_transform(dataset_tain.Exterior2nd)

dataset_tain.ExterCond=labelencoder_X.fit_transform(dataset_tain.ExterCond)
dataset_tain.ExterQual=labelencoder_X.fit_transform(dataset_tain.ExterQual)
dataset_tain.Foundation=labelencoder_X.fit_transform(dataset_tain.Foundation)
dataset_tain.Heating=labelencoder_X.fit_transform(dataset_tain.Heating)
dataset_tain.HeatingQC=labelencoder_X.fit_transform(dataset_tain.HeatingQC)
dataset_tain.CentralAir=labelencoder_X.fit_transform(dataset_tain.CentralAir)
dataset_tain.KitchenQual=labelencoder_X.fit_transform(dataset_tain.KitchenQual)
dataset_tain.Functional=labelencoder_X.fit_transform(dataset_tain.Functional)
dataset_tain.PavedDrive=labelencoder_X.fit_transform(dataset_tain.PavedDrive)
dataset_tain.SaleType=labelencoder_X.fit_transform(dataset_tain.SaleType)
dataset_tain.SaleCondition=labelencoder_X.fit_transform(dataset_tain.SaleCondition)
############################################################################
dataset_tain.Alley=labelencoder_X.fit_transform(dataset_tain.Alley)
dataset_tain.MasVnrType=labelencoder_X.fit_transform(dataset_tain.MasVnrType)
dataset_tain.BsmtQual=labelencoder_X.fit_transform(dataset_tain.BsmtQual)
dataset_tain.BsmtCond=labelencoder_X.fit_transform(dataset_tain.BsmtCond)
dataset_tain.BsmtExposure=labelencoder_X.fit_transform(dataset_tain.BsmtExposure)
dataset_tain.BsmtFinType1=labelencoder_X.fit_transform(dataset_tain.BsmtFinType1)
dataset_tain.BsmtFinType2=labelencoder_X.fit_transform(dataset_tain.BsmtFinType2)
dataset_tain.Electrical=labelencoder_X.fit_transform(dataset_tain.Electrical)
dataset_tain.FireplaceQu=labelencoder_X.fit_transform(dataset_tain.FireplaceQu)
dataset_tain.GarageType=labelencoder_X.fit_transform(dataset_tain.GarageType)
dataset_tain.GarageFinish=labelencoder_X.fit_transform(dataset_tain.GarageFinish)
dataset_tain.GarageQual=labelencoder_X.fit_transform(dataset_tain.GarageQual)
dataset_tain.GarageCond=labelencoder_X.fit_transform(dataset_tain.GarageCond)
dataset_tain.PoolQC=labelencoder_X.fit_transform(dataset_tain.PoolQC)
dataset_tain.Fence=labelencoder_X.fit_transform(dataset_tain.Fence)
dataset_tain.MiscFeature=labelencoder_X.fit_transform(dataset_tain.MiscFeature)

dataset_tain=dataset_tain.replace("NA",100)

#################################################################
onehotencoder= OneHotEncoder(categorical_features=[2])
dataset_tain=onehotencoder.fit_transform(dataset_tain).toarray()
onehotencoder9= OneHotEncoder(categorical_features=[9])
dataset_tain=onehotencoder9.fit_transform(dataset_tain).toarray()
onehotencoder11= OneHotEncoder(categorical_features=[11])
dataset_tain=onehotencoder11.fit_transform(dataset_tain).toarray()
onehotencoder14= OneHotEncoder(categorical_features=[14])
dataset_tain=onehotencoder14.fit_transform(dataset_tain).toarray()
onehotencoder18= OneHotEncoder(categorical_features=[18])
dataset_tain=onehotencoder18.fit_transform(dataset_tain).toarray()
onehotencoder22= OneHotEncoder(categorical_features=[22])
dataset_tain=onehotencoder22.fit_transform(dataset_tain).toarray()
onehotencoder24= OneHotEncoder(categorical_features=[24])
dataset_tain=onehotencoder24.fit_transform(dataset_tain).toarray()
onehotencoder29= OneHotEncoder(categorical_features=[29])
dataset_tain=onehotencoder29.fit_transform(dataset_tain).toarray()
onehotencoder32= OneHotEncoder(categorical_features=[32])
dataset_tain=onehotencoder32.fit_transform(dataset_tain).toarray()
onehotencoder57= OneHotEncoder(categorical_features=[57])
dataset_tain=onehotencoder57.fit_transform(dataset_tain).toarray()
onehotencoder66= OneHotEncoder(categorical_features=[66])
dataset_tain=onehotencoder66.fit_transform(dataset_tain).toarray()
onehotencoder74= OneHotEncoder(categorical_features=[74])
dataset_tain=onehotencoder74.fit_transform(dataset_tain).toarray()
onehotencoder79= OneHotEncoder(categorical_features=[79])
dataset_tain=onehotencoder79.fit_transform(dataset_tain).toarray()
onehotencoder91= OneHotEncoder(categorical_features=[91])
dataset_tain=onehotencoder91.fit_transform(dataset_tain).toarray()
onehotencoder97= OneHotEncoder(categorical_features=[97])
dataset_tain=onehotencoder97.fit_transform(dataset_tain).toarray()
onehotencoder105= OneHotEncoder(categorical_features=[105])
dataset_tain=onehotencoder105.fit_transform(dataset_tain).toarray()
onehotencoder120= OneHotEncoder(categorical_features=[120])
dataset_tain=onehotencoder120.fit_transform(dataset_tain).toarray()
onehotencoder136= OneHotEncoder(categorical_features=[136])
dataset_tain=onehotencoder136.fit_transform(dataset_tain).toarray()
onehotencoder146= OneHotEncoder(categorical_features=[146])
dataset_tain=onehotencoder146.fit_transform(dataset_tain).toarray()
onehotencoder151= OneHotEncoder(categorical_features=[151])
dataset_tain=onehotencoder151.fit_transform(dataset_tain).toarray()
onehotencoder157= OneHotEncoder(categorical_features=[157])
dataset_tain=onehotencoder157.fit_transform(dataset_tain).toarray()
onehotencoder162= OneHotEncoder(categorical_features=[162])
dataset_tain=onehotencoder162.fit_transform(dataset_tain).toarray()
onehotencoder167= OneHotEncoder(categorical_features=[167])
dataset_tain=onehotencoder167.fit_transform(dataset_tain).toarray()
onehotencoder172= OneHotEncoder(categorical_features=[172])
dataset_tain=onehotencoder172.fit_transform(dataset_tain).toarray()
onehotencoder180= OneHotEncoder(categorical_features=[180])
dataset_tain=onehotencoder180.fit_transform(dataset_tain).toarray()
onehotencoder190= OneHotEncoder(categorical_features=[190])
dataset_tain=onehotencoder190.fit_transform(dataset_tain).toarray()
onehotencoder196= OneHotEncoder(categorical_features=[196])
dataset_tain=onehotencoder196.fit_transform(dataset_tain).toarray()
onehotencoder201= OneHotEncoder(categorical_features=[201])
dataset_tain=onehotencoder201.fit_transform(dataset_tain).toarray()
onehotencoder203= OneHotEncoder(categorical_features=[203])
dataset_tain=onehotencoder203.fit_transform(dataset_tain).toarray()
onehotencoder219= OneHotEncoder(categorical_features=[219])
dataset_tain=onehotencoder219.fit_transform(dataset_tain).toarray()
onehotencoder224= OneHotEncoder(categorical_features=[224])
dataset_tain=onehotencoder224.fit_transform(dataset_tain).toarray()
onehotencoder232= OneHotEncoder(categorical_features=[232])
dataset_tain=onehotencoder232.fit_transform(dataset_tain).toarray()
onehotencoder240= OneHotEncoder(categorical_features=[240])
dataset_tain=onehotencoder240.fit_transform(dataset_tain).toarray()
onehotencoder244= OneHotEncoder(categorical_features=[244])
dataset_tain=onehotencoder244.fit_transform(dataset_tain).toarray()
onehotencoder250= OneHotEncoder(categorical_features=[250])
dataset_tain=onehotencoder250.fit_transform(dataset_tain).toarray()
onehotencoder256= OneHotEncoder(categorical_features=[256])
dataset_tain=onehotencoder256.fit_transform(dataset_tain).toarray()
onehotencoder262= OneHotEncoder(categorical_features=[262])
dataset_tain=onehotencoder262.fit_transform(dataset_tain).toarray()
onehotencoder272= OneHotEncoder(categorical_features=[272])
dataset_tain=onehotencoder272.fit_transform(dataset_tain).toarray()
onehotencoder276= OneHotEncoder(categorical_features=[276])
dataset_tain=onehotencoder276.fit_transform(dataset_tain).toarray()
onehotencoder281= OneHotEncoder(categorical_features=[281])
dataset_tain=onehotencoder281.fit_transform(dataset_tain).toarray()
onehotencoder289= OneHotEncoder(categorical_features=[289])
dataset_tain=onehotencoder289.fit_transform(dataset_tain).toarray()
onehotencoder298= OneHotEncoder(categorical_features=[298])
dataset_tain=onehotencoder298.fit_transform(dataset_tain).toarray()

######################################################################################################
dataset_test.MSZoning=labelencoder_X.fit_transform(dataset_test.MSZoning)
dataset_test.Street=labelencoder_X.fit_transform(dataset_test.Street)
dataset_test.LotShape=labelencoder_X.fit_transform(dataset_test.LotShape)
dataset_test.LandContour=labelencoder_X.fit_transform(dataset_test.LandContour)
dataset_test.Utilities=labelencoder_X.fit_transform(dataset_test.Utilities)
dataset_test.LotConfig=labelencoder_X.fit_transform(dataset_test.LotConfig)
dataset_test.LandSlope=labelencoder_X.fit_transform(dataset_test.LandSlope)
dataset_test.Neighborhood=labelencoder_X.fit_transform(dataset_test.Neighborhood)
dataset_test.Condition1=labelencoder_X.fit_transform(dataset_test.Condition1)
dataset_test.Condition2=labelencoder_X.fit_transform(dataset_test.Condition2)
dataset_test.BldgType=labelencoder_X.fit_transform(dataset_test.BldgType)
dataset_test.HouseStyle=labelencoder_X.fit_transform(dataset_test.HouseStyle)
dataset_test.RoofStyle=labelencoder_X.fit_transform(dataset_test.RoofStyle)
dataset_test.RoofMatl=labelencoder_X.fit_transform(dataset_test.RoofMatl)
dataset_test.Exterior1st=labelencoder_X.fit_transform(dataset_test.Exterior1st)
dataset_test.Exterior2nd=labelencoder_X.fit_transform(dataset_test.Exterior2nd)

dataset_test.ExterCond=labelencoder_X.fit_transform(dataset_test.ExterCond)
dataset_test.ExterQual=labelencoder_X.fit_transform(dataset_test.ExterQual)
dataset_test.Foundation=labelencoder_X.fit_transform(dataset_test.Foundation)
dataset_test.Heating=labelencoder_X.fit_transform(dataset_test.Heating)
dataset_test.HeatingQC=labelencoder_X.fit_transform(dataset_test.HeatingQC)
dataset_test.CentralAir=labelencoder_X.fit_transform(dataset_test.CentralAir)
dataset_test.KitchenQual=labelencoder_X.fit_transform(dataset_test.KitchenQual)
dataset_test.Functional=labelencoder_X.fit_transform(dataset_test.Functional)
dataset_test.PavedDrive=labelencoder_X.fit_transform(dataset_test.PavedDrive)
dataset_test.SaleType=labelencoder_X.fit_transform(dataset_test.SaleType)
dataset_test.SaleCondition=labelencoder_X.fit_transform(dataset_test.SaleCondition)
############################################################################
dataset_test.Alley=labelencoder_X.fit_transform(dataset_test.Alley)
dataset_test.MasVnrType=labelencoder_X.fit_transform(dataset_test.MasVnrType)
dataset_test.BsmtQual=labelencoder_X.fit_transform(dataset_test.BsmtQual)
dataset_test.BsmtCond=labelencoder_X.fit_transform(dataset_test.BsmtCond)
dataset_test.BsmtExposure=labelencoder_X.fit_transform(dataset_test.BsmtExposure)
dataset_test.BsmtFinType1=labelencoder_X.fit_transform(dataset_test.BsmtFinType1)
dataset_test.BsmtFinType2=labelencoder_X.fit_transform(dataset_test.BsmtFinType2)
dataset_test.Electrical=labelencoder_X.fit_transform(dataset_test.Electrical)
dataset_test.FireplaceQu=labelencoder_X.fit_transform(dataset_test.FireplaceQu)
dataset_test.GarageType=labelencoder_X.fit_transform(dataset_test.GarageType)
dataset_test.GarageFinish=labelencoder_X.fit_transform(dataset_test.GarageFinish)
dataset_test.GarageQual=labelencoder_X.fit_transform(dataset_test.GarageQual)
dataset_test.GarageCond=labelencoder_X.fit_transform(dataset_test.GarageCond)
dataset_test.PoolQC=labelencoder_X.fit_transform(dataset_test.PoolQC)
dataset_test.Fence=labelencoder_X.fit_transform(dataset_test.Fence)
dataset_test.MiscFeature=labelencoder_X.fit_transform(dataset_test.MiscFeature)

dataset_test=dataset_test.replace("NA",100)

#################################################################
onehotencoder= OneHotEncoder(categorical_features=[2])
dataset_test=onehotencoder.fit_transform(dataset_test).toarray()
onehotencoder10= OneHotEncoder(categorical_features=[10])
dataset_test=onehotencoder10.fit_transform(dataset_test).toarray()
onehotencoder12= OneHotEncoder(categorical_features=[12])
dataset_test=onehotencoder12.fit_transform(dataset_test).toarray()
onehotencoder15= OneHotEncoder(categorical_features=[15])
dataset_test=onehotencoder15.fit_transform(dataset_test).toarray()
onehotencoder19= OneHotEncoder(categorical_features=[19])
dataset_test=onehotencoder19.fit_transform(dataset_test).toarray()
onehotencoder23= OneHotEncoder(categorical_features=[23])
dataset_test=onehotencoder23.fit_transform(dataset_test).toarray()
onehotencoder25= OneHotEncoder(categorical_features=[25])
dataset_test=onehotencoder25.fit_transform(dataset_test).toarray()
onehotencoder30= OneHotEncoder(categorical_features=[30])
dataset_test=onehotencoder30.fit_transform(dataset_test).toarray()
onehotencoder33= OneHotEncoder(categorical_features=[33])
dataset_test=onehotencoder33.fit_transform(dataset_test).toarray()
onehotencoder58= OneHotEncoder(categorical_features=[58])
dataset_test=onehotencoder58.fit_transform(dataset_test).toarray()
onehotencoder67= OneHotEncoder(categorical_features=[67])
dataset_test=onehotencoder67.fit_transform(dataset_test).toarray()
onehotencoder72= OneHotEncoder(categorical_features=[72])
dataset_test=onehotencoder72.fit_transform(dataset_test).toarray()
onehotencoder77= OneHotEncoder(categorical_features=[77])
dataset_test=onehotencoder77.fit_transform(dataset_test).toarray()
onehotencoder88= OneHotEncoder(categorical_features=[88])
dataset_test=onehotencoder88.fit_transform(dataset_test).toarray()
onehotencoder94= OneHotEncoder(categorical_features=[94])
dataset_test=onehotencoder94.fit_transform(dataset_test).toarray()
onehotencoder98= OneHotEncoder(categorical_features=[98])
dataset_test=onehotencoder98.fit_transform(dataset_test).toarray()
onehotencoder112= OneHotEncoder(categorical_features=[112])
dataset_test=onehotencoder112.fit_transform(dataset_test).toarray()
onehotencoder128= OneHotEncoder(categorical_features=[128])
dataset_test=onehotencoder128.fit_transform(dataset_test).toarray()
onehotencoder134= OneHotEncoder(categorical_features=[134])
dataset_test=onehotencoder134.fit_transform(dataset_test).toarray()
onehotencoder138= OneHotEncoder(categorical_features=[138])
dataset_test=onehotencoder138.fit_transform(dataset_test).toarray()
onehotencoder143= OneHotEncoder(categorical_features=[143])
dataset_test=onehotencoder143.fit_transform(dataset_test).toarray()
onehotencoder149= OneHotEncoder(categorical_features=[149])
dataset_test=onehotencoder149.fit_transform(dataset_test).toarray()
onehotencoder154= OneHotEncoder(categorical_features=[154])
dataset_test=onehotencoder154.fit_transform(dataset_test).toarray()
onehotencoder159= OneHotEncoder(categorical_features=[159])
dataset_test=onehotencoder159.fit_transform(dataset_test).toarray()
onehotencoder164= OneHotEncoder(categorical_features=[164])
dataset_test=onehotencoder164.fit_transform(dataset_test).toarray()
onehotencoder172= OneHotEncoder(categorical_features=[172])
dataset_test=onehotencoder172.fit_transform(dataset_test).toarray()
onehotencoder182= OneHotEncoder(categorical_features=[182])
dataset_test=onehotencoder182.fit_transform(dataset_test).toarray()
onehotencoder186= OneHotEncoder(categorical_features=[186])
dataset_test=onehotencoder186.fit_transform(dataset_test).toarray()
onehotencoder191= OneHotEncoder(categorical_features=[191])
dataset_test=onehotencoder191.fit_transform(dataset_test).toarray()
onehotencoder193= OneHotEncoder(categorical_features=[193])
dataset_test=onehotencoder193.fit_transform(dataset_test).toarray()
onehotencoder207= OneHotEncoder(categorical_features=[207])
dataset_test=onehotencoder207.fit_transform(dataset_test).toarray()
onehotencoder213= OneHotEncoder(categorical_features=[213])
dataset_test=onehotencoder213.fit_transform(dataset_test).toarray()
onehotencoder222= OneHotEncoder(categorical_features=[222])
dataset_test=onehotencoder222.fit_transform(dataset_test).toarray()
onehotencoder228= OneHotEncoder(categorical_features=[228])
dataset_test=onehotencoder228.fit_transform(dataset_test).toarray()
onehotencoder236= OneHotEncoder(categorical_features=[236])
dataset_test=onehotencoder236.fit_transform(dataset_test).toarray()
onehotencoder242= OneHotEncoder(categorical_features=[242])
dataset_test=onehotencoder242.fit_transform(dataset_test).toarray()
onehotencoder247= OneHotEncoder(categorical_features=[247])
dataset_test=onehotencoder247.fit_transform(dataset_test).toarray()
onehotencoder253= OneHotEncoder(categorical_features=[253])
dataset_test=onehotencoder253.fit_transform(dataset_test).toarray()
onehotencoder262= OneHotEncoder(categorical_features=[262])
dataset_test=onehotencoder262.fit_transform(dataset_test).toarray()
onehotencoder265= OneHotEncoder(categorical_features=[265])
dataset_test=onehotencoder265.fit_transform(dataset_test).toarray()
onehotencoder270= OneHotEncoder(categorical_features=[270])
dataset_test=onehotencoder270.fit_transform(dataset_test).toarray()
onehotencoder277= OneHotEncoder(categorical_features=[277])
dataset_test=onehotencoder277.fit_transform(dataset_test).toarray()
onehotencoder287= OneHotEncoder(categorical_features=[287])
dataset_test=onehotencoder287.fit_transform(dataset_test).toarray()
onehotencoder265= OneHotEncoder(categorical_features=[265])
dataset_test=onehotencoder265.fit_transform(dataset_test).toarray()
#Removing Dummy variable trap
dataset_tain=dataset_tain[:,1:]
dataset_test=dataset_test[:,1:]

X_train=dataset_tain[:,:-1]
y_train=dataset_tain[:,299]
X_test=dataset_test[:,:]

#fitting multiple linear regression to training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_test)







