#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:49:05 2021

@author: jeffreykirshenbaum
"""
#parta.Sorting by part description)

invoices = [(83, 'Electric sander', 7, 57.98),
            (24, 'Power saw', 18, 99.99),
            (7, 'Sledge hammer', 11, 21.50),
            (77,'Hammer', 76, 11.99),
            (39, 'Jig saw', 3, 79.50)]
from operator import itemgetter

for part, desc, quant, price in sorted(invoices, key=itemgetter(1)):
    print(f'{part:>2} {desc:<16} {quant:>3}{price:7.2f}')
    
#Part b.): Sorting by quantity      
for part, desc, quant, price in sorted(invoices, key=itemgetter(3)):
    print(f'{part:>2}{desc:<16}{quant:>3}{price:7.2f}')


#Partc.)sorting by price 
quantities = [(desc, quant) for part, desc, quant, price in invoices ]

for desc, quant in sorted(quantities, key=itemgetter(1)):
    print(f'{desc:<16}{quant:>3}')


#partd. sorting by invoice value.)

invoice = [(desc,quant*price) for part, desc, quant, price in invoices]
for desc, product in sorted(invoice, key=itemgetter(1)):
    print(f'{desc:<20}{product:<10}')
    
    
    
#parte.) Filitering to invoice values in (200,500))


invoice = [(desc,quant*price) for part, desc, quant, price in invoices
    if 200 <= quant*price <=500]
    
for desc, product in sorted(invoice, key=itemgetter(1)):
    print(f'{desc:<30}{product:<25}')
    
#part f.) Finding total invoices


total = 0
for part, desc, quant, price in invoices:
    total += (quant*price)
    
print("total of invoice values is", total)