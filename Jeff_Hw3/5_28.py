#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:41:33 2021

@author: jeffreykirshenbaum
"""

import numpy as np

"""Twenty students were asked to rate on a scale of 1 to 5 the quality of 
the food in the student cafeteria, with 1 being “awful” and 5 
being “excellent.” Place the 20 responses in a list
1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5
Determine and display the frequency of each rating. Use the 
built-in functions, statis- tics module functions and NumPy functions 
demonstrated in Section 5.17.2 to display the following response statistics: 
    minimum, maximum, range, mean, median, mode, vari- ance and standard 
    deviation. """

responses= [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

values,frequency=np.unique(responses, return_counts=True)
 
print(f'values   {values}\nfrequency{frequency}')

import statistics as stat

print("the mean is", stat.mean(responses))
print("the max is", max(responses))
print("the min is", min(responses))
print("the pop. standard deviation is", stat.pstdev(responses))
print("the sample standard deviation is", stat.stdev(responses))
print("the populaiton variance is",stat.pvariance(responses))
print("the sample variance is",stat.variance(responses))

print("the range is", max(responses)-min(responses))
print("the mode is", stat.mode(responses))
print("the median is", stat.median(responses))