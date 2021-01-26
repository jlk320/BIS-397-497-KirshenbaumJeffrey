#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:14:05 2021

@author: jeffreykirshenbaum
"""

import numpy as np
import random



%timeit list1 = \
   [random.randrange(1, 7) for i in range(0, 1)]
   
   
%timeit list10 = \
   [random.randrange(1, 7) for i in range(0, 10)]
   
%timeit list100 = \
   [random.randrange(1, 7) for i in range(0, 100)]
   
%timeit list1_000 = \
   [random.randrange(1, 7) for i in range(0, 1_000)]
   
%timeit list10_000 = \
   [random.randrange(1, 7) for i in range(0, 10_000)]
%timeit list100_000 = \
   [random.randrange(1, 7) for i in range(0, 100_000)]
   
%timeit list1_000_000 = \
   [random.randrange(1, 7) for i in range(0, 1_000_000)]
                                          



                                         
%timeit array1 = np.random.randint(1, 7, 1)
%timeit array10 = np.random.randint(1, 7, 10)
%timeit array100 = np.random.randint(1, 7, 100)
%timeit array1_000 = np.random.randint(1, 7, 1_000)
%timeit array10_000 = np.random.randint(1, 7, 10_000)
%timeit array100_000 = np.random.randint(1, 7, 100_000)
%timeit array1_000_000 = np.random.randint(1, 7, 1_000_000)



tuple_list=('8.56 µs ± 194 ns per loop ','79.2 µs ± 348 ns per loop ', 
        '814 µs ± 32.8 µs per loop ', '8.04 ms ± 54.1 µs per loop', '80.8 ms ± 513 µs per loop ', 
        '825 ms ± 18.1 ms per loop ', '1.3 µs ± 25.9 ns per loop ')

tuple_array=('13.7 µs ± 1.62 µs per loop',
             '14.5 µs ± 971 ns per loop ', '14.8 µs ± 1.46 µs per loop',
             '27.2 µs ± 3.8 µs per loop ', '135 µs ± 8.98 µs per loop ', 
             '1.09 ms ± 59.9 µs per loop', '13.9 ms ± 1.13 ms per loop')
tuple_number_values=("1        ", "10       ", "100      ","1_000    ","10_000   ","100_000  ",
                     "1_000_000")


array_tuple_list=np.array((tuple_list)).reshape(7,1) 
array_tuple_array=np.array((tuple_array)).reshape(7,1)
array_number_values=np.array((tuple_number_values)).reshape(7,1)

total=np.hstack((array_tuple_list, array_tuple_array))

total_=np.hstack((array_number_values,total))
print("#Values  ", "    List Average Execution Time  ","Array Average Execution Time")
print(total_)  