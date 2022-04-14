# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 05:44:14 2022

@author: tavakoli
"""

m=int(input("enter your row: "))
n=int(input("enter your col: "))
for i in range(1,m+1):
    for j in range(1,n+1):
        print(i*j,end=" ")
    print()