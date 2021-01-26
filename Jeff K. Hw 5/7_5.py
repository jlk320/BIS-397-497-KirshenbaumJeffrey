#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:30:51 2021

Create a 2-by-3 array containing the first six powers of 2 
beginning with 2. Flatten the array first with method flatten, then with ravel. 
In each case, display the result then display the original array to show that it 
was unmodified."""






#creating 2 by 3 array
import numpy as np

two_array=np.array([2**0,2**1,2**2,2**3,2**4,2**5]).reshape(2,3)
#printing 2 by 3 array
print(two_array)
#flattening and raveling
flattened = two_array.flatten()
raveled = two_array.ravel()
#showing flattened and ravelled and original
print(flattened)
print(raveled)
print(two_array)


