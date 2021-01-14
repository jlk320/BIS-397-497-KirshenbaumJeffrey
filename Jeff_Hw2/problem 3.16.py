#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:19:44 2021

@author: jeffreykirshenbaum
"""

#Problem 3.16 (finished)


largest = int(input('Enter Integer Here: '))
number = int(input('Enter Integer Here: '))


if largest>number:
   next_largest=number
   
else:
    next_largest=largest
    largest=number
    
for counter in range (2,10):
    number = int(input('Enter Integer Here: '))
    if number > largest: 
        next_largest=largest
        largest=number
    elif number>next_largest:
        next_largest=number

print ('The Largest Integer is:',largest)
print ('The Second Largest Integer is:',next_largest)