# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:12:28 2020

@author: dmulhall
"""

file = 'input.txt'

with open(file) as f:
    lines = f.readlines()

lines = list(map(int, lines))

for num in lines:
    
    for num1 in lines:
        for num2 in lines:
            if num + num1 + num2 == 2020:
                print('Found - {} + {} +{} = 2020'.format(num,num1,num2))
                print(num1*num*num2)