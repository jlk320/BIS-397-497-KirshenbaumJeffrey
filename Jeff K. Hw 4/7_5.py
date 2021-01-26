#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:30:51 2021

Create a 2-by-3 array containing the first six powers of 2 
beginning with 2. Flatten the array first with method flatten, then with ravel. 
In each case, display the result then display the original array to show that it 
was unmodified."""






import numpy as np

two_array=np.array([2** i for i in range(6)]).reshape(2,3)

two_array


two_array.flatten()
two_array
two_array.ravel()
two_array


