# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:37:30 2020

@author: dmulhall
"""
import re 

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
  
def string_to_dict(passport):
    full_passport = ''
    for l in passport:
        full_passport = full_passport + ' ' + l
    
    d = re.findall(r"[\w']+", full_passport)
    
    #d = dict(full_passport.split(":") for full_passport in str.split(";"))    
    return Convert(d)

def part_1(passport, valid):
    ids = list(passport)
    
    for i in valid:
        if i not in ids:
            return 0
    return 1

def part_2(passport, valid):
    ids = list(passport)
    
    ecl_val = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    
    for i in valid:
        if i not in ids:
            return 0
    for key, val  in passport.items():
        print(key, val)
        if key == 'ecl':
            if val not in ecl_val:
                return 0 
        if key == 'byr':
            if 120 >= int(val) >= 2002:
                return 0 
        if key =='iyr':
             if 2010 >= int(val) >= 2020:
                return 0            
        if key == 'eyr':
              if 2020 >= int(val) >= 2030:
                return 0             
        if key == 'hgt':
            if val[-2:] =='cm':
                if 150 >= val[:-2] >= 193:
                    return 0 
            if val[-2:] =='in':
                if 59 >= val[:-2] >= 76:
                    return 0 
        if key == 'hcl':
            if val[0] != '#'
                return 0
            if val[-1:] not
        
    return 1

file = 'test.txt'

with open(file) as f:
    lines = f.readlines()
    
lines = [i.split('\n', 1)[0] for i in lines]


valid_id = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    

no_valid = 0
passport = []

dict_pass = {}
cnt = 0

for l in lines:
    if (l == '') or (l == lines[-1]):
        #print(passport)
        if l == lines[-1]:
            passport.append(l)
        dict_pass[cnt] = string_to_dict(passport)
        cnt += 1
        passport = []
    else:
        passport.append(l)



for d in dict_pass:
   #print(dict_pass[d])
   no_valid += part_2(dict_pass[d], valid_id)
    
print(no_valid)
