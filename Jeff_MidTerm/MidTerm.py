#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 15:02:18 2021

@author: jeffreykirshenbaum
"""
"""
Assume that you are using a battleship game board that has 10 columns (A through J) 
and 10 rows (1 through 10). I want you 
to write a program that will generate random "shots" by matching a randomly 
selected column and row from the appropriate ranges (e.g., "B3"), showing that 
shot on the console, and then waiting for input from the user. If the user inputs 
"N", the program will generate another shot; if the user inputs "H", it will generate 
the statement "You sank their battleship!" and then terminate.
A complete solution will also include error checking for other inputs, 

prompting the user that they have entered an invalid key 
and asking them to try again. """

#importing random module
 
import random


#creating random shot function
def random_shot():
    row=random.randrange(1,11)
    column=random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    print("New Shot is",column,row,end='')
    

user_input=0
#Generating Initial Random Shot 
row=random.randrange(1,11)
column=random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
print("Shot is",column,row,end='')

#Creating While Loop to Continue Game Until Ship Sinks    
while user_input!="H":
    
    user_input=input("Did The Battleship Get Hit? (N if no, H if yes): ")
    
    if user_input=="N":
        print("You Missed! Shoot Again")
        random_shot()
                   
    elif user_input=="H":
        print("You sank their battleship!")
        break
    else: 
        print("You have entered an invalid key. Please Try Again.")
        
 
    

    
    