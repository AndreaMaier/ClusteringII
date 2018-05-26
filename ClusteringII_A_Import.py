# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:41:35 2018

@author: Andrea
"""

import pandas as pd
import numpy as np

def read_Data():
    data = pd.read_csv('../../data/vienna_sights.csv', delimiter=',')
    #data.fillna(np.nan)
    return data
