#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:20:31 2021

@author: jeffreykirshenbaum
"""

# Problem 4.9 (Finished,)
#Fahrenheit= (9/5)*C+32


print(' C', '      F')
for C in range (0,101):
    F = (9/5)*C+32
    print(f'{C:>2}{F:>10.1f}')
    


