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

data = preparedData.data_Transformation()

def distance_matrix():
    length = max(data.index)+1
    distance_matrix = np.empty([length, length])
    for i in data.index:
        for j in data.index:
            if i in data.index and j in data.index:
                p1_long = data['longitude'][i]
                p1_lat = data['latitude'][i]
                p2_long = data['longitude'][j]
                p2_lat = data['latitude'][j]
                distance_long = (p1_long - p2_long) * 71500
                distance_lat = (p1_lat - p2_lat) * 111300
                distance_matrix[i][j] = math.sqrt(math.pow(distance_long,2)+math.pow(distance_lat,2))
    return distance_matrix

distance_matrix = distance_matrix()
            
#TO DO Perform Clustering