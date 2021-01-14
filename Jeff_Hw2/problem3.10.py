#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:19:05 2021

@author: jeffreykirshenbaum
"""

#Problem 3.10 (Finshed, but ask about labels)
import decimal
from decimal import Decimal

print ("year",' money') 
principal = Decimal('1000.00')
rate = Decimal('0.07')
for year in range(1, 31):
    amount = principal * (1 + rate) ** year 
    print(f'{year:>2}{amount:>10.2f}')