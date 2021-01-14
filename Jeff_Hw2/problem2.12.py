#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:17:49 2021

@author: jeffreykirshenbaum
"""

# Problem 2.12 (Finished)



import decimal
from decimal import Decimal

# Calculating Money After 10 years

principal=1000
rate=.07
money_10 = principal * (1 + rate) **10
print(f'After 10 Years, you will have ${money_10:>8.2f}')
#Calculating Money After 20 years 

principal=1000
rate=.07
money_20 = principal * (1 + rate) **20
print(f'After 20 Years, you will have ${money_20:>8.2f}')
#Calculating Money After 30 Years 

principal=1000
rate=.07
money_30 = principal * (1 + rate) **30
money_30

print(f'After 30 Years, you will have ${money_30:>8.2f}')




