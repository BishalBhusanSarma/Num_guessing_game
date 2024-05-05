# This will import the random module
import random

numb = random.randint(1, 100) # This will generate random number between 1 and 100.
count = 0
attmp = 0

# Telling the player that he/she has only 5 attempts.
print("\nYou have 5 attempts to solve it!!")

# Creating a loop. If we don't get the number, the loop will not stop.
while True:

    guessed_num= int(input("\nGuess a number between 1 and 100 : "))
    
    count+=1
    attmp+=1
       

    # Checking, if the guessed number is equal to the random generated number.       
    if guessed_num == numb:
        print("\n**You guessed it right**")

    elif guessed_num > numb:
        print("\nyou have", 5-count,"attempts left")
        print("\n**Guess a smaller one** ")
        
    else:
        print("\nyou have", 5-count,"attempts left")
        print("\n**Guess a bigger one** ")


    # Asking the player if he wants to restart the game after wasting all the attempts.
    if count == 5:
        print("\nYou are out of attempts")
        yesorno = input("\nDo you want to restart? Y/N : ")
        
        if yesorno == "Y" or yesorno == "y":
            count = 0
        elif yesorno == "N" or yesorno == "n":
            break       # to exit from this 'while' loop

        else:
            print("\nInvalid Parameters")
            break       # to exit from this 'while' loop



print("\nyou guessed the right number in", attmp, "attempts")
