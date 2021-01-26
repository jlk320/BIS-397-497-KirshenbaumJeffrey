#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
create an array containing the values 1–15, reshape it into a 3-by-5 array, 
then use indexing and slicing techniques to perform each of the following operations:
a) Selectrow2.
b) Select column 5.
c) Select rows 0 and 1.
d) Select columns 2–4.
e) Selecttheelementthatisinrow1andcolumn4.
f) Select all elements from rows 1 and 2 that are in columns 0, 2 and 4.."""

# creating array contianing values: 1-15

import numpy as np

array = np.arange(1,16).reshape(3,5)
print(array)

#a.) Selecting row 2
array[2]
print(array[2])

#b.) Selecting Column 5
array[:,4]
print(array[:,4])

#c.) Select rows 0 and 1
array[0:2]
print(array[0:2])

#d.) Select Columns 2 through 4
array[:,2:5]
print(array[:,2:5])


#e.) Selecting element that is in row 1 and column 4
array[1,4]
print(array[1,4])

#f.) Selecting all elements from rows 1,2 that are in columns 0,2,4
array[1:3,[0,2,4]]
print(array[1:3,[0,2,4]])

