# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 00:58:30 2022

@author: tavakoli
"""
import random
boys=['ali','reza','yasin','benyamin','mehrdad','sajjad','aidin','shahin']
girls=['sara','zari','neda','homa','eli','goli','mary','mina']
zoj=[]
for i in range(len(boys)):
    boy=random.choice(boys)
    girl=random.choice(girls)
    boys.remove(boy)
    girls.remove(girl)
    zoj.append((boy,girl))
print(zoj)    