# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 05:30:34 2022

@author: asreno
"""

import numpy as np
row=int(input())
col=int(input())
arr1=np.full((row,col),0)
row1=int(input())
col1=int(input())
arr2=np.full((row1,col1),1)
arr3=np.vstack([arr1,arr2])

print(arr3)