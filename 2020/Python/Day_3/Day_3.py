# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:20:30 2020

@author: dmulhall
"""
import re 
  

file = 'input.txt'

with open(file) as f:
    lines = f.readlines()
    
lines = [i.split('\n', 1)[0] for i in lines]


total_trees = []

slopes = [(1,False), (3,False), (5,False), (7,False), (1,True)]

for s in slopes:
    right = s[0]
    x = s[0]
    skip_line = s[1]
    cnt = 1
    trees = 0

    for l in lines[1:]:
        
        if skip_line:
            if cnt % 2 == 0:
            
                #print(len(l))
                if x >= len(l):
                    x = x - len(l)
                
                #print(x)
                    
                if l[x] == '#':
                    trees += 1
                #print(l)
                #print(l[x])
            
                x = x + right
    
        else:
            #print(len(l))
            if x >= len(l):
                x = x - len(l)
            
            #print(x)
                
            if l[x] == '#':
                trees += 1
            #print(l)
            #print(l[x])
        
            x = x + right
            
        cnt +=1

    print('Number of Trees = {}'.format(trees))
    total_trees.append(trees)

Result = 1

for t in total_trees:
    Result = Result*t
    
print(Result)