# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:31:02 2020

@author: dmulhall
"""

def decode_seat(seat):
    
    row = seat[:7]
    col = seat[-3:]
    #print(seat)
    #print(row,col)
    
    x = 2**6
    row_num = 0
    for s in row:
        if s =='B':
            row_num = row_num +x
        x = x/2
    
    y = 2**2
    col_num = 0   
    for s in col:
       if s =='R':
           col_num = col_num +y
       y = y/2   
    
    #print((row_num*8) + col_num)
    return (row_num*8) + col_num

file = 'input.txt'

with open(file) as f:
    lines = f.readlines()
    
lines = [i.split('\n', 1)[0] for i in lines]

all_seats = []

for l in lines:
    all_seats.append(decode_seat(l))
    
print(max(all_seats))
print(min(all_seats))
print(len(all_seats))


for i in range(int(max(all_seats))):
    if i not in all_seats:
        print(i)


