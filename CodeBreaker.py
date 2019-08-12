# -*- coding: utf-8 -*-
"""
@author: Zachary Moore
@description: This program imitates the minigame Adventure Decoder in Maplestory in a console. 
The minigame is having the user think logically in order to guess a specific 
number combination within a certain number of rounds.

TODO: 
    implement timer for each round, 
    number of correct digits and numbers
"""
#import sys      #for getting params from command line
import random as rd

#checks number (as a string) if it contains a duplicate value (i.e. 4553 is invalid, but 4567 is valid)
def checkDuplicateValues(num):
    #create and populate list of digits in num
    lst = []
    for c in num:
        lst.append(c)
    
    #check if list of digits contains all unique elements
    #True (or all unique values) 
    return len(set(lst)) == len(lst)

#compares the number the user entered and the random number
def compareNumbers(user, rand):
    index = 0
    digit_places = 0
    values_in_number = 0
    print(user, rand)
    while index < len(rand):
        if user[index] == rand[index]:
            digit_places += 1
        index += 1
           
    if index == len(rand):
        return True
    else:
        return False

#prints keypad instructions
def printKeypad(digits):
    print("123456789")
    print("Please enter a " + str(digits) + " digit number consisting of the above numbers: ")

#gets the range for randomizing a code
def getMinMax(digits):
    range_min = 1 * 10**digits       #expression on right is for exponent 
    range_max = 9 * 10**digits
    digits -= 1
    digit = 9
    while digits > -1:
        range_max += digit*10**digits
        digits -= 1
    
    return range_min, range_max
    
def playGame(rounds, digits, max_digits):
    roundnum = 1
    history = list()#dict()
    while roundnum < (rounds + 1):
        #print history
        #timer = 0
        print("Guess History:")
        for s in history:
            print(s)
        
        #get range for random int
        selected_number = 0
        while(True):
            range_min, range_max = getMinMax(digits)
            selected_number = rd.randint(range_min, range_max)
            print("Selected number: " + str(selected_number))
            if checkDuplicateValues(selected_number):
                break
        #print keypad
        #printKeypad(digits)
        #get user input
        while(True):
            printKeypad(max_digits)
            user_choice = input()
            if len(user_choice) == max_digits and user_choice.isdigit() and checkDuplicateValues(user_choice):
                break
        #compare numbers to determine accuracy
        result = compareNumbers(user_choice, str(selected_number))
        if result:
            print("Congrats! You guessed the right number!")
            return
        else:
            print("Wrong Number! Try Again!")
            history.append(user_choice)
        
        #increment round number
        roundnum += 1

#prints game instructions
def printInstructions(digits, rounds):
    print("Type a " + str(digits) + " digit number and use logic to guess the correct number")
    print("The number after X is number of digits not in the correct number")
    print("The number after T is number of digits in the correct number, but not correct digit position")
    print("The number after O is number of digits both in correct number and in right digit position")
    print("You get " + str(rounds) + " attempts to guess the number")

def run():
    flag = False
    rounds = 10 #TODO: set to param entered
    max_digits = 4
    printInstructions(max_digits, rounds)
    digits = max_digits - 1     #decrement digits to get correct selected number
    garbage = input()
    while (True):
        if flag:
            #check if user wants to play again
            print("Do you want to play another game? (y or n): ")
            choice = input()
            print("You chose " + choice)
            if choice is "n":
                print("Exiting")
                return
        #play game
        playGame(rounds, digits, max_digits)
        flag = True
        

if __name__ == '__main__':
    run()