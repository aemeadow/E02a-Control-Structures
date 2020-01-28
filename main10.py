#!/usr/bin/env python3
import sys, random
# imports the things we need

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"
# makes sure the user can run the program 


print('Greetings!')
# opening greeting typed to the user 
colors = ['red','orange','yellow','green','blue','violet','purple']
# defines colors as these things, with a backup "violet" for purple 
play_again = ''
# empty quotes so it will play again once ending
best_count = sys.maxsize            # the biggest number
# as your comment suggests, it defines best count as the biggest number 

while (play_again != 'n' and play_again != 'no'):
    # the option for the user to end the loop, but while thats not ended, for the loop to continue
    match_color = random.choice(colors)
    # defines goal color as a randomized choice from the colors array
    count = 0
    # sets the count to 0 
    color = ''
    # sets the color to nothing yet 
    while (color != match_color):
        #  when the guessed color is not the random pick, it will ask again 
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        # prompts the input question for what the color could be 
        color = color.lower().strip()
        # makes sure that no case or space will falter this program 
        count += 1
        # adds one count to the guesses count during the loop 
        if (color == match_color):
            # if the user guesses correctly then this
            print('Correct!')
            # a congrats 
        else:
            # if not correct 
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
            # when they are wrong, informs of current guess count and the loop restarts
    
    print('\nYou guessed it in {} tries!'.format(count))
    # after correct guess, this result informs of the amount of guesses 

    if (count < best_count):
        # if the count now is less than the previous highest number, then it is the new best 
        print('This was your best guess so far!')
        # a result message for the user if this is the result 
        best_count = count
        # assigns the best count to be connected to the count 

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()
    # asks if the player wants to play again, and if n or no, it will turn off. 

print('Thanks for playing!')
# a final message 