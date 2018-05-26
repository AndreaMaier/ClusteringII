# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:11:25 2018

@author: Andrea
"""

import ClusteringII_A_Import as importData
import pandas as pd
import numpy as np

def data_Cleaning():
    data = importData.read_Data()
    
    data = data.drop(['www'], axis=1)
    data = data.drop(['City'], axis=1)
    data = data.drop(['Street'], axis=1)
    keys = data.keys()
    for key in keys:
        index = data[data[key].isnull()].index
        for i in index:
            data = data.drop([i])
            
    #for i in data['latitude']:
        #print(i)
        
    print('\n')
    #for i in data.index:
        #print(i, data['longitude'][i])
    data = data.drop(10)
    return data

def data_Transformation():
    data = data_Cleaning()
    for i in data.index:
        data['longitude'][i] = float(data['longitude'][i])
    return data
