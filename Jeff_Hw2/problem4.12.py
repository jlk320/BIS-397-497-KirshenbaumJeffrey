#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:21:32 2021

@author: jeffreykirshenbaum
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:42:47 2021

@author: jeffreykirshenbaum
"""

import random

race_end = 70 

#Creating rarndom variable for tortoise move
def move_tortoise(tortoise):
    move = random.randrange(1,11)
    
    if 1 <= move <= 5:
        tortoise +=3
    elif move in (6,7):
        tortoise -= 6
    else: 
        tortoise +=1
        
    if tortoise <1:
        tortoise = 1
    elif tortoise > race_end:
        tortoise = race_end
    return tortoise 

#creating a random variable for hare move
def move_hare(hare):
    move = random.randrange(1,11)
    
    if move in (3,4):
        hare += 9
    elif move == 5:
        hare -= 12
    elif 6 <= move <=8:
        hare += 1
    elif move >8:
        hare -= 2
 #adjusting to hare not being able to move to left of posiiton one   
    if hare <1:
        hare = 1
    elif hare > race_end:
        hare = race_end 
    
    return hare

#printing positions along the way of the game 
def print_positions(tortoise, hare): 
    
    for count in range (1, race_end + 1):
        if count == tortoise and count == hare:
            print('OUCH!!!', end='')
        elif count == hare:
            print('H', end='')
        elif count == tortoise:
            print('T', end='')
        else:
            print(' ', end='')
    print()
    
    
tortoise = 1
hare = 1
timer = 0
#Initial on your mark, get set, go statements 
print('ON YOUR MARK, GET SET')
print('BANG !!!!!')
print("AND THEY'RE OFF !!!!!")


while tortoise < race_end and hare < race_end:
    hare = move_hare(hare)
    tortoise = move_tortoise(tortoise)
    print_positions(tortoise, hare)
    timer +=1
    
if tortoise >= hare:
    print('\nTORTOISE WINS!! YAY!!!')
else: 
    print('\nHare wins. Yuch!')
print(f'TIME ELAPSED = {timer} seconds')
    