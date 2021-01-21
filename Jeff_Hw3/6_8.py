#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:24:24 2021

@author: jeffreykirshenbaum
"""

number_to_word = {
    0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR',
    5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE',
    10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 
    14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN', 17: 'SEVENTEEN',
    18: 'EIGHTEEN', 19: 'NINETEEN', 20: 'TWENTY', 21: 'Twenty-One', 
    22: 'Twenty Two', 23: 'Twenty Three', 24: 'Twenty Four', 25: 'Twenty Five',
    26: 'Twenty Six', 27: 'Twenty Seven', 28: 'Twenty Eight', 29: 'Twenty Nine',
    30: 'Thirty', 31: 'Thirty One', 32: 'Thirty Two', 33: 'Thirty Three', 34: 'Thirty Four',
    35: 'Thrity Five', 36: 'Thirty Six', 37: 'Thirty Seven', 38: 'Thirty Eight', 39: 'Thirty Nine',
    40: 'Forty', 41:'Forty One', 42: 'Forty Two', 43: 'Forty Three', 44: 'Forty Four', 45: 'Forty Five', 
    46: 'Forty Six', 47: 'Forty Seven', 48: 'Forty Eight', 49: 'Forty Nine', 50: 'Fifty', 
    51: 'Fifty One', 52: 'Fifty Two', 53: 'Fifty Three', 54: 'Fifty Four', 
    55: 'Fifty Five', 56: 'Fifty Six', 57: 'Fifty Seven', 58: 'Fifty Eight', 
    59: 'Fifty Nine', 60: 'Sixty', 61: 'Sixty One', 62: 'Sixty Two', 63: 'Sixty Three',
    64: 'Sixty Four', 65: 'Sixty Five', 66: 'Sixty Six', 67: 'Sixty Seven', 68: 'Sixty Eight', 
    69: 'Sixty Nine', 70: 'Seventy', 71: 'Seventy One', 72: 'Seventy Two',
    73: 'Seventy Three', 74: 'Seventy Four', 75: 'Seventy Five', 76: 'Seventy Six',
    77: 'Seventy Seven', 78: 'Seventy Eight', 79: 'Seventy Nine', 80: 'Eighty',
    81: 'Eighty One', 82: 'Eighty Two', 83: 'Eighty Three', 84: 'Eighty Four', 
    85: 'Eighty Five', 86: 'Eighty Six', 87: 'Eighty Seven', 88: 'Eighty Eight',
    89: 'Eighty Nine', 90: 'Ninety', 91: 'Ninety One', 92: 'Niney Two', 93: 'Ninety Three', 
    94: 'Ninety Four', 95: 'Ninety Five', 96: 'Ninety Six', 97: 'Ninety Seven',
    98: 'Ninety Eight', 99: 'Ninety Nine'
}   

 
numbers_to_word_keys = number_to_word.keys()    

numbers_to_word_keys 
keys_numbers=list(numbers_to_word_keys )


amount=input('Enter a dollar amount less than 1000.00: ')
dollars, cents = amount.split('.')
dollars = int(dollars)
cents = int(cents)
amount_in_words = []

if 0<= dollars < 100:
    amount_in_words.append(number_to_word[dollars])
    amount_in_words.append("AND")
    amount_in_words.append(keys_numbers[cents])
    first, second, third = amount_in_words
    fourth = '/100'
    print(first, second, third, fourth, end='')
elif (dollars ==100 or dollars ==200 or dollars==300 \
or dollars == 400 or dollars ==500 or dollars ==600 or dollars ==700 \
or dollars == 800 or dollars==900):
    amount_in_words.append(number_to_word[dollars // 100])
    amount_in_words.append("Hundred AND")
    amount_in_words.append(keys_numbers[cents])
    first, second, third = amount_in_words
    fourth = '/100'
    print(first, second, third, fourth, end='')
elif dollars >=100:
    amount_in_words.append(number_to_word[dollars // 100])
    amount_in_words.append("Hundred")
    amount_in_words.append(number_to_word[dollars % 100])
    amount_in_words.append("AND")
    amount_in_words.append(keys_numbers[cents])
    first, second, third, fourth, fifth = amount_in_words
    sixth = '/100'
    print(first, second, third, fourth, fifth, sixth)
    
    
    

    


    
    
    
    
    
    


    
   
