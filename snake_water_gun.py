# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 17:48:24 2023

@author: lab
"""

import random

print("Snake water gun game")

# choice = int(input("Input: "))

# while(True):
#     if()
    # pass

def game():
    print("Enter 1/2/3 snake, gun and water respectively")
    try:
        while True:
            user_choice = int(input("Enter 1/2/3:\n"))
            # random.choice takes iterable
            computer_turn = random.randint(1, 3)
            
            print("You:", user_choice)
            print("Computer:", computer_turn)
            
            if user_choice == computer_turn:
                print("Draw")
            elif (user_choice == 3 and computer_turn == 1)                          or (user_choice == 3 and computer_turn == 2) or (user_choice == 1 and computer_turn == 3):
                print("User wins!")
            else:
                print("Computer wins")
                
            if user_choice not in [1,2,3]:
                print("Not a valid number!")
            
    except ValueError:
        print("Incorrect input")

game()







