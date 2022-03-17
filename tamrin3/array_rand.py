# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 00:50:44 2022

@author: tavaloi

"""
import random
random_numbers=[]
number=int(input("enter your number: "))
for i in range(number):
    rand_number= random.randint(0,50)
    if rand_number not in random_numbers:
        random_numbers.append(rand_number)
print("your array is: ",random_numbers)        