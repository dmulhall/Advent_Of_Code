# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:02:00 2020

@author: dmulhall
"""
def count_list(l2):
    list1 =[]
    len_1 = len(l2)
    for l in l2:
        list1 = list1 + split(l)
    my_dict = {i:list1.count(i) for i in list1}
    #print(my_dict)
    num = 0
    for key in my_dict:
        if my_dict[key] == len_1:
            num = num + 1
    #print(num)            
    return num

def split(word): 
    return [char for char in word]  

file = 'input.txt'

with open(file) as f:
    lines = f.readlines()
    
lines = [i.split('\n', 1)[0] for i in lines]




from itertools import groupby
line1 = [list(g) for k, g in groupby(lines, key=bool) if k]

print(line1)

cus_form = []
for l in line1:
    single_form = []
    for s in l:
        if len(s) > 1:
            for s1 in split(s):
                single_form.append(s1)
        else:
            single_form.append(s)

    cus_form.append(set(single_form))
                    
                
print(cus_form)
cnt = 0
for f in cus_form:
    cnt = cnt +len(f)
    

    
print(cnt)


cnt1 = 0
cus_form = []
for l in line1:
    print(l)
    if len(l) == 1:
        cnt1 = cnt1 + len(l[0])
    else:
        cnt1 = cnt1 + count_list(l)
        #single_form.append(s)

print(cnt1)