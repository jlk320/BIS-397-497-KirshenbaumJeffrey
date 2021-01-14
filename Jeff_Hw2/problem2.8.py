#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:17:11 2021

@author: jeffreykirshenbaum
"""

# Problem 2.8 (Finsihed)

##Do print statement with headings prior to forloop
print('Numbers','Squared ', 'Cubed ')
for numbers in range (1,6):

    squared_numbers = numbers ** 2 
    cubed_numbers= numbers**3 
    print (numbers, '\t   ', squared_numbers, '\t    ', cubed_numbers)



