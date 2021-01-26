#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:21:02 2021

@author: jeffreykirshenbaum
"""
#Creating list of even integers

"""Create a 3-by-3 array containing the 
even integers from 2 through 18. Create a 
second 3-by-3 array containing the integers from 9 down to 1,
 then multiply the first array by the second."""


import numpy as np


even_array= np.arange(2,20,2).reshape(3,3)
print(even_array)

#Creating of 9 down to 1 in reverse
reverse_array=np.arange(9,0,-1).reshape(3,3)
print(reverse_array)

#Multiplying together 

multiplied_array =  even_array*reverse_array

print(multiplied_array)


