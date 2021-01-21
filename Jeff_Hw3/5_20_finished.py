#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:01:23 2021

@author: jeffreykirshenbaum
"""

def create_table(lists_, column_width):
    indent = len(str(len(lists_)))
    print(f'{"":{indent}}', end='')
    
    for col in range(len(lists_[0])):
        print(f'{col:>{column_width}}', end='')
    print()
    
    for i, row in enumerate(lists_):
        print(f'{i:>{indent}}',end='')
        for value in row:
            print(f'{value:>{column_width}}', end='')
            
        print()
        
lists = [[1,2,5,6,7,8,4],[2,5,3,6,7,8,4],[3,5,6,7,4,2,1]]


create_table(lists,6)
