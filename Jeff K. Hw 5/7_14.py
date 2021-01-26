#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:03:51 2021

@author: jeffreykirshenbaum
"""
"""
Create the two-dimensional arrays array1 = np.array([[0, 1], [2, 3]])
       array2 = np.array([[4, 5], [6, 7]])
a) Use vertical stacking to create the 4-by-2 
array named array3 with array1 stacked on top of array2.
b) Use horizontal stacking to create the 2-by-4 
array named array4 with array2 to the right of array1.
c) Useverticalstackingwithtwocopiesof
array4tocreatea4-by-4array5.
d) Use horizontal stacking with 
two copies of array3 to create a 4-by-4 array6.

"""
import numpy as np

array1= np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])
#a.) Creating a 4 by 2 matrix by vertical stack 
array3=np.vstack((array1,array2))
print(array3)

#b.) Creating a 2 by 4 matrix using horizontal stack

array4=np.hstack((array1,array2))
print(array4)

#c.) Creeating a 4 by 4 using two copies of array 4

array4_copy=array4.copy()

array5=np.vstack((array4,array4_copy))

print(array5)

#d.) 
array3_copy=array3.copy()

array6=np.hstack((array3,array3_copy))
print(array6)



