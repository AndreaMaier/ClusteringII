# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:46:58 2018

@author: Andrea
"""

import ClusteringII_C_DataPreparation as preparedData
import pandas as pd
import numpy as np
from geopy.distance import vincenty
import math
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import pdist, squareform
from math import *

data = preparedData.data_Transformation()
data_lonlat = data.drop(['name'], axis=1)

def haversine(lonlat1, lonlat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lat1, lon1 = lonlat1
    lat2, lon2 = lonlat2
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

distance_matrix = squareform(pdist(data_lonlat, (lambda u,v: haversine(u,v))))
print(distance_matrix)

db = DBSCAN(eps=0.35, min_samples=2, metric="precomputed")
db.fit_predict(distance_matrix)
print(db.labels_)
print(len([i for i in db.labels_ if i == -1]))
data['cluster']=db.labels_
print(data)