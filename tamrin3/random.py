# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 21:09:03 2022

@author: tavakoli
"""

number=int(input("enter your number: "))

for i in range(number):
    if i%2 ==0:
        print("[]", end=" ")
    else:
        print("{}", end=" ")
        
	