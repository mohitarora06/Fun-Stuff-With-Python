# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

secret_number = 0
number_of_guesses = 0
number_range = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, number_of_guesses, number_range
    print ""
    print 'New game. Range is from o to', str(number_range)   
    secret_number = random.randrange(0, number_range)
    number_of_guesses = math.ceil(math.log(number_range, 2))
    print "Number of remaining guesses is ", str(number_of_guesses)
    # remove this when you add your code    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number_range
    
    number_range = 100
    new_game()
    # remove this when you add your code    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global number_range
    
    number_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number, number_of_guesses
    
    number = float(guess)
    print ""
    print "Guess was ", guess
    
    number_of_guesses -= 1
    print "Number of remaining guesses is ", str(number_of_guesses)
    
    if secret_number > number:
        print 'Higher'
    elif secret_number < number:
        print 'Lower'
    else:
        print 'Correct'
        new_game()

    if number_of_guesses == 0:
        print 'You are out of number of guesses'
        new_game()
        
    # remove this when you add your code
    
# create frame

frame = simplegui.create_frame('Mind Game', 500, 500)
# register event handlers for control elements and start frame
frame.add_button('Range is [0,100)', range100, 200)
frame.add_button('Range is [0,1000)', range1000, 200)
frame.add_input('Enter your guess', input_guess, 200)
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
