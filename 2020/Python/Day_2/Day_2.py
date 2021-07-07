# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:26:35 2020

@author: dmulhall
"""

import re 

def split(word): 
    return [char for char in word]  

file = 'input.txt'

with open(file) as f:
    lines = f.readlines()
    
#lines = lines[:10]
    
#lines = [i.split('\n', 1)[0] for i in lines]

line_split = []

for l in lines:
    line_split.append(l.split(':'))
 
line_split_2 = line_split.copy()  
 
for i, l in enumerate(line_split):
    line_split_2[i][0] = re.findall(r"[\w']+", l[0])

num_wrong_pass = 0
num_right_pass = 0

for l in line_split_2:
    min_letter = int(l[0][0])
    max_letter = int(l[0][1])
    letter = l[0][2]
    chars = split(l[1])
    #print(min_letter, max_letter, letter, l[1])
    if letter in l[1]:
        index_list = [i for i, e in enumerate(chars) if e == letter]
       # print(index_list)
        if min_letter in index_list and max_letter in index_list:
        #    print('Incorrect\n')
            num_wrong_pass += 1
        elif min_letter not in index_list and max_letter not in index_list:
         #   print('Incorrect\n')
            num_wrong_pass += 1           
        else:
          #  print('Correct\n')
            num_right_pass += 1
    else:
        num_wrong_pass += 1
    # if min_letter > count or count > max_letter:
    #       num_wrong_pass += 1
    # else:
    #     num_right_pass += 1

        
print(num_wrong_pass)
print(num_right_pass)

