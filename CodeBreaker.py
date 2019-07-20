# -*- coding: utf-8 -*-
"""
Created on 7/20/2019 
@author: Zachary Moore
@description: this program imitates the minigame code breaker in Maplestory. 
The minigame is having the user think logically in order to guess a specific 
number combination within a certain number of rounds.

TODO: implement game instructions, timer for each round, number repitition limit (i.e. 5865)
"""
#import sys      #for getting params from command line
import random as rd

def compareNumbers(user, rand):
    index = 0
    correct_count = 0
    while user[index] == rand[index]:
        correct_count += 1
        index += 1
        
    if index == len(rand):
        return True
    else:
        return False

def printKeypad(digits):
    print("123456789")
    print("Please enter a %d digit number consisting of the above numbers: ", digits)

def getMinMax(digits):
    range_min = 1 * 10**digits       #expression on right is for exponent 
    range_max = 9 * 10**digits
    digits -= 1
    digit = 9
    while digits > -1:
        range_max += digit*10**digits
        digits -=1
    
    return range_min, range_max
    
def playGame(rounds, digits):
    roundnum = 1
    history = list()#dict()
    while roundnum < (rounds + 1):
        #print history
        print("Guess History:")
        for s in history:
            print(s)
        
        #get range for random int
        range_min, range_max = getMinMax(digits)
        selected_number = rd.randint(range_min, range_max)
        #print keypad
        printKeypad(digits)
        #get user input
        user_choice = input()
        #compare numbers to determine accuracy
        result = compareNumbers(user_choice, str(selected_number))
        if result:
            print("Congrats! You guessed the right number!")
            return
        else:
            history.append(user_choice)
        
        #increment round number
        roundnum += 1

def run():
    flag = False
    rounds = 10 #TODO: set to param entered
    digits = 4
    while (True):
        if flag:
            #check if user wants to play again
            print("Do you want to play another game? (y or n): ")
            choice = input()
            print("You chose " + choice)
            if choice is "n":
                print("Exiting")
                exit()
        playGame(rounds, digits)
        flag = True
        

if __name__ == '__main__':
    run()