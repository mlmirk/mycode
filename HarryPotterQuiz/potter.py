#!/usr/bin/env python3
from questionBank import QandA
"""Michael Mikrovic
  Miniproject 1 using loops and conidtionals to create a small game 
  of Harry potter hard trivia"""


validAnswers= ['1','2','3','4']

#caluculats win percentage based on 
#correct answers vs Total number of questions
def calcWinPercentage(correcAnswers):
    return 100*(correcAnswers/QandA.__len__())

#Looks for a q first for player quitting check for case and extra space
#then see if its a valid answer chopping off space and sending 
#sending int back to be checked agast the stored answer
def getUserGuess():
    while True:
        guess=input("Choose the number of the correct answer:\n")
        if guess.upper().replace(" ","") == "Q":
            return "Q"
        elif guess.replace(" ","") in validAnswers:
            return int(guess)
        else:
            print('Enter a valid guess 1-4')

#Check if answer == guess
def checkAnswer(answer,guess):
    if answer == guess:
        print("\nCorrect!")
        return True
    else:
        print("\nNope!")
        return False
        
 #prints questions and calls other functions to check 
 # and validate user input       
def questions():
    correctAnswers=0
    print("PRESS Q TO QUIT AT ANY TIME \n ")
    for x in range(QandA.__len__()):
        print(f"{QandA[x]['Question']}")
        print(f"1. {QandA[x][1]}")
        print(f"2. {QandA[x][2]}")
        print(f"3. {QandA[x][3]}")
        print(f"4. {QandA[x][4]}")
        answer= QandA[x]["A"]
        guess = getUserGuess()
        #Break out of loop if user quits
        if guess == 'Q':
            print("you quit the quiz score calulated on answered questions")
            break
        if checkAnswer(answer,guess):
            correctAnswers+=1
        print("***************************")
    percentage = calcWinPercentage(correctAnswers)
    print(f"Your final score was {percentage} you got\n{correctAnswers} out of {QandA.__len__()} questions")       

#user input to play case insentive and extra space ignored
def playGame():
    x=True
    while x == True:
        play = input("Do you want to play harry potter trivia? [Y] or any other key to quit\n")
        if play.upper().replace(" ","") == "Y":
            questions()
            break
        else: 
            break

def main():
    playGame()

        
if __name__ == "__main__":
    main()          





