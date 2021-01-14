#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:18:21 2021

@author: jeffreykirshenbaum
"""

# fig03_03.py
"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures

# process 10 students
'below is the modified portion of the code'

counter=passes + failures
while counter<10:
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))

    if result == 1:
        passes = passes + 1
        counter=passes+failures
    elif result==2:
        failures = failures + 1
        counter=passes+failures
    else:
        print ("Invalid Input, Enter 1 or 2")
'end of modified portion'

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')