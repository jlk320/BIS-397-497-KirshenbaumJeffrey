#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:52:53 2021

@author: jeffreykirshenbaum
"""

text =input('Input a Sentence Here: ')
texts=text.lower()

word_counts = {}
duplicates=0

# count occurrences of each unique word
for word in texts.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

   
word_counts
for word in word_counts:
    if word_counts[word] > 1:
        duplicates+=1
print(f'There are {duplicates} duplicate words in the sentence')
