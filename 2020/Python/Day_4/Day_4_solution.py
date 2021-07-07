# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:09:57 2020

@author: dmulhall
"""
import re

# Open the input file
inputfile = open('input.txt', 'r')

# Parse lines
data = [x.strip() for x in inputfile.readlines()]

def valid(passport):
    # Validate mandatory fields
    fields = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid']
    for f in fields:
        if(f not in passport):
            return False

    # Validate numerical
    if not ( 1920 <= int(passport['byr']) <= 2002):
        return False
    if not ( 2010 <= int(passport['iyr']) <= 2020):
        return False
    if not ( 2020 <= int(passport['eyr']) <= 2030):
        return False

    # Validate Height
    if 'cm' in passport['hgt'] and not (150 <= int(passport['hgt'][:-2]) <=193):
        return False
    elif 'in' in passport['hgt'] and not (59 <= int(passport['hgt'][:-2]) <= 76):
        return False
    if 'cm' not in passport['hgt'] and 'in' not in passport['hgt']:
        return False

    # Validate strings/enums
    if  passport['ecl'] not in ['amb', 'blu', 'brn','gry','grn','hzl','oth']:
        return False
    if re.match(r'^\#[0-9a-f]{6}$', passport['hcl']) is None:
        return False
    if re.match(r'^\d{9}$', passport['pid']) is None:
        return False

    return True

def part2(data):
    valid_passport_count = 0
    current = {}
    for line in data:
        if line == '':
            if valid(current):
                valid_passport_count += 1
            current = {}
            continue

        for field in line.split():
            field,val = field.split(':')
            current[field] = val
    return valid_passport_count


print( "Solution part 1: %d" % part2(data))