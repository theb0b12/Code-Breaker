# -*- coding: utf-8 -*-
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
def compareNumbers(user, rand, max_digits):
    count_x = 0
    count_t = 0
    count_o = 0
    user_lst = [c for c in user]
    
    #print(user, rand)
    
    for i in range(len(user_lst)):
        if user_lst[i] not in rand:
            count_x += 1
        else:
            match = False
            for j in range(len(rand)):
                if user_lst[i] == rand[j]:
                    match = True
                    break
            if match:
                count_o += 1
            else:
                count_t += 1
    
    #return whether the number was found and list of the counts (as strings)
    return max_digits == count_o, [str(count_x), str(count_t), str(count_o)]

#prints keypad instructions
def printKeypad(digits):
    print("Please enter a " + str(digits) + " digit number with no duplicate values: ")

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
    history = list()    #list of dictionaries (since dictionaries can't hold duplicate keys)
    entry = dict()      #key is the attempted combination and value is result list
    
    #get range for random int
    selected_number = 0
    while(True):
        range_min, range_max = getMinMax(digits)
        selected_number = rd.randint(range_min, range_max)
        #print("Selected number: " + str(selected_number))
        if checkDuplicateValues(str(selected_number)):
            break
    
    while roundnum < (rounds + 1):
        #print history
        #timer = 0
        print("Guess History:")
        for entry in history:
            for key in entry:
                print(key + "- X:" + entry[key][0] + " | T:" + entry[key][1] + " | O:" + entry[key][2])
        
        
        #print keypad and get user input
        while(True):
            printKeypad(max_digits)
            user_choice = input()
            if len(user_choice) == max_digits and user_choice.isdigit() and checkDuplicateValues(user_choice):
                break
            print("Incorrect input. Please try again")
        #compare numbers to determine accuracy
        number_found, result = compareNumbers(user_choice, str(selected_number), max_digits)
        if number_found:
            print("Congrats! You guessed the right number!")
            return
        else:
            print("Wrong Number! Try Again!")
            entry[user_choice] = result
            history.append(entry)
        
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
    rounds = 5 #TODO: set to param entered
    max_digits = 3
    printInstructions(max_digits, rounds)
    digits = max_digits - 1     #decrement max_digits to get correct selected number 
    print("Enter any key to continue")
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