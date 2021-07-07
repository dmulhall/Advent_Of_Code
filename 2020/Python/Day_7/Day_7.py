# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:05:29 2020

@author: dmulhall
"""
def check_rule(rule, bag):
    
    bag5 = rule[0] +' ' + rule[1]
    
    if rule[4] == 'no':
        return None
    elif len(rule) > 17:
        bag1 = rule[5] + ' ' + rule[6]
        bag2 = rule[9] + ' ' +  rule[10]
        bag3 = rule[13] + ' ' +  rule[14]
        bag4 = rule[17] + ' ' +  rule[18]
        if bag == bag1 or bag == bag2 or bag == bag3 or bag == bag4:
            return bag5
        else:
            return None
    elif 17 > len(rule) > 13:
        bag1 = rule[5] + ' ' + rule[6]
        bag2 = rule[9] + ' ' +  rule[10]
        bag3 = rule[13] + ' ' +  rule[14]
        if bag == bag1 or bag == bag2 or bag == bag3:
            return bag5
        else:
            return None
    elif 13 > len(rule) > 8:
        bag1 = rule[5] + ' ' + rule[6]
        bag2 = rule[9] + ' ' +  rule[10]
        if bag == bag1 or bag == bag2:
            return bag5
        else:
            return None
    else:
        bag1 = rule[5] + ' ' + rule[6]
        if bag == bag1:
           return bag5
        else:
           return None
        

def part_2(rule, bag):
    
    bag5 = rule[0] +' ' + rule[1]
    
    if rule[4] == 'no':
        return None
    elif len(rule) > 17:
        bag1 = rule[5] + ' ' + rule[6]
        bag2 = rule[9] + ' ' +  rule[10]
        bag3 = rule[13] + ' ' +  rule[14]
        bag4 = rule[17] + ' ' +  rule[18]
        if bag == bag1 or bag == bag2 or bag == bag3 or bag == bag4:
            return bag5
        else:
            return None
    elif 17 > len(rule) > 13:
        bag1 = rule[5] + ' ' + rule[6]
        bag2 = rule[9] + ' ' +  rule[10]
        bag3 = rule[13] + ' ' +  rule[14]
        if bag == bag1 or bag == bag2 or bag == bag3:
            return bag5
        else:
            return None
    elif 13 > len(rule) > 8:
        bag1 = rule[5] + ' ' + rule[6]
        bag2 = rule[9] + ' ' +  rule[10]
        if bag == bag1 or bag == bag2:
            return bag5
        else:
            return None
    else:
        bag1 = rule[5] + ' ' + rule[6]
        if bag == bag1:
           return bag5
        else:
           return None
        

file = 'test2.txt'

with open(file) as f:
    lines = f.readlines()
    
lines = [i.split('\n', 1)[0] for i in lines]


rules = []
bag = 'shiny gold'

for l in lines:
    rules.append(l.split())

print(rules)
print()

bags = []
checked_bags = []
search = True
finished = False
bags.append(bag)

while search:
    start = len(bags)
    for r in rules:
        bags.append(check_rule(r, bag))
    
    bags = [i for i in bags if i] 
    
    end = len(bags)
    checked_bags.append(bag)
    
    checked_bags_s = set(checked_bags)
 
    if start == end:
        search = False   
 
    for b in bags:
        if b not in checked_bags:
            bag = b
            search = True

    

    print(checked_bags_s)
    print(bags)

print(len(checked_bags_s))
    