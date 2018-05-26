# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:51:05 2018

@author: Andrea
"""

import ClusteringII_A_Import as importData
import pandas as pd
import numpy as np

data = importData.read_Data()

def Data_Understanding():
    print(data.count())
    print(data.keys())
    print(data.info())
    print(data.describe())
    print(data['name'].describe())
    print(data['Street'].describe())
    print(data['City'].describe())
    print(data['longitude'].describe())
    print(data['www'].describe())