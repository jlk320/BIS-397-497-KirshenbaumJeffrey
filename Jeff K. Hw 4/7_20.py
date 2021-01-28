#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:14:05 2021

@author: jeffreykirshenbaum
"""
#Importing Needed Functions
import numpy as np
import random
import pandas as pd


list1 = %timeit -o [random.randrange(1,7) for i in range (0,1)]
list10 = %timeit -o [random.randrange(1,7) for i in range (0,10)]
list100 = %timeit -o [random.randrange(1,7) for i in range (0,100)]
list1_000 = %timeit -o [random.randrange(1,7) for i in range (0,1_000)]
list10_000 = %timeit -o [random.randrange(1,7) for i in range (0,10_000)]
list100_000 = %timeit -o [random.randrange(1,7) for i in range (0,100_000)]
list1_000_000 = %timeit -o [random.randrange(1,7) for i in range (0,1_000_000)]





                                         

array1 = %timeit -o np.random.randint(1,7,1)
array10 = %timeit -o np.random.randint(1,7,10)
array100 = %timeit -o np.random.randint(1,7,100)
array1_000 = %timeit -o np.random.randint(1,7,1_000)
array10_000 = %timeit -o np.random.randint(1,7,10_000)
array100_000 = %timeit -o np.random.randint(1,7,100_000)
array1_000_000 = %timeit -o np.random.randint(1,7,1_000_000)


#Creating Dictionary of %timeout output results
timeit_dic={"List Avgerage. Execution Time": [list1,list10,list100,
                                            list1_000,list10_000,list100_000,
                                            list1_000_000], "Array Average. Execution Time":
            [array1,array10,array100,array1_000,array10_000, array100_000,
            array1_000_000]}
#Converting Dictionary to data frame to make it look like a table   
table=pd.DataFrame(timeit_dic)
table.index=[1,10,100,1_000,10_000,100_000,1_000_000]
print(table)



"""This Produced a Really bad looking table. However, I wasn't sure how to 
get rid of the unnecessary part of the %timeit output that said:
    "(mean ± std. dev. of 7 runs, 1000000 loops each)". So, I copy and pasted 
    the output and re-did the whole process to make the table more readable. 
    If there is a way to do this automatically, rather than manually like I did,
    I would really appreciate learning about it in your feedback. """

#Copy and Pasting %timeit output but not including irrelevant info. Doing 
#this to make it shorter
list1='2.42 µs ± 360 ns per loop'
list10 = '14.7 µs ± 3.69 µs per loop'
list100 = '86.8 µs ± 12.6 µs per loop'
list1_000 = '805 µs ± 7.29 µs per loop'
list10_000 = '8.18 ms ± 268 µs per loop'
list100_000 = '135 ms ± 59.9 ms per loop'
list1_000_000 = '1.45 s ± 310 ms per loop'

array1 = '14.3 µs ± 1.36 µs per loop'
array10 = '18.6 µs ± 2.98 µs per loop'
array100 =  '14.4 µs ± 2 µs per loop'
array1_000 = '23.7 µs ± 494 ns per loop'
array10_000 = '121 µs ± 3.78 µs per loop'
array100_000 = '1.09 ms ± 77.2 µs per loop'
array1_000_000 = '11.6 ms ± 279 µs per loop'



#creating new dictionary with more readable output
timeit_dic_={"List Avgerage. Execution Time": [list1,list10,list100,
                                            list1_000,list10_000,list100_000,
                                            list1_000_000], "Array Average. Execution Time":
            [array1,array10,array100,array1_000,array10_000, array100_000,
            array1_000_000]}
 #creating a more readable dable    
table_=pd.DataFrame(timeit_dic_)
table_.index=[1,10,100,1_000,10_000,100_000,1_000_000]
print(table_)

