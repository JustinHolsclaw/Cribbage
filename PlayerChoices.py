import random

from Deal_Shuffle import Deal_Shuffle
from gameRules import gameRules
Rules = gameRules
Deal = Deal_Shuffle

def Menu():
    option1 = 'Play'
    option2 = 'Exit'
    print("Welcome to the Cribbage Game Alpha")
    print("Please Select an option")
    print('1 {option1}')
    print('2 {option2}')

    validChoice = False
    while validChoice == False:
        choice = input("Enter your choice with the corresponding number: ")
        if choice == '1':
            playGame()
        elif choice == '2':
            validChoice = True
        else:
            choice = input("Invalid input, please submit a new number: ")
        

def playGame():
    BothHands = Deal().DealAndShuffle()
    x = 0
    while x < 6:
        hand1 = BothHands[x]
        hand2 = BothHands[x+5]
        wildCard = BothHands[13]
        x = x+1
    
    def chooseCards():
        print(" Player 1 Please select the cards that you want to put into the crib by typing in the number of the card based on its order in the hand")
        print (hand1)
        validChoice = False
        while validChoice == False:
            choice = input("Enter your choice with the corresponding number: ")
            if choice == '1':
                playGame()
            elif choice == '2':
                validChoice = True
            else:
                choice = input("Invalid input, please submit a new number: ")
        
    
