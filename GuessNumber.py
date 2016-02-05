# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code

num_range = 100 #range of the random number
random_num = 0 #random number selected for the game
num_guess = 0 #number of guesses left to player

# helper function to start and restart the game
def new_game():
    global random_num, num_guess
    
    #generates random number
    random_num = random.randrange(0,num_range)
    
    #sets the correct number of guesses based on range
    if num_range == 100:
        num_guess = 7
    else:
        num_guess = 10
    
    #game inizialization
    print("New game. Range is from 0 to " + str(num_range))
    print("Number of remaining guesses is: " + str(num_guess))
    print("")
    
    frame.start()


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) 
    global num_range
    num_range = 100
    
    #restarts
    new_game()    


def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000

    #restarts
    new_game()  
    
def input_guess(guess):
    # main game logic goes here	
    global num_guess
    
    # new number of guesses
    num_guess = num_guess - 1
    
    #Got the correct number        
    if int(guess) == random_num: 
        print("Guess was " + guess)
        print("Number of remaining guesses is " + str(num_guess))
        print("Correct!")
        print("")
        
        #restarts
        new_game()
    
    #non correct number, run out of guesses
    elif num_guess == 0:
        print("Guess was " + guess) 
        print("Number of remaining guesses is " + str(num_guess))
        print("You ran out of guesses. The number was " + str(random_num))
        print("")
            
        #restarts
        new_game()
            
    #non correct number, more guesses still possible    
    else:        
        # guess is bigger than number
        if int(guess) > random_num:
            print("Guess was " + guess)
            print("Number of remaining guesses is " + str(num_guess))
            print("Lower!")        
            print("")
         
        # guess is smaller than number    
        elif int(guess) < random_num:
            print("Guess was " + guess)
            print("Number of remaining guesses is " + str(num_guess))
            print("Higher!")        
            print("")  
            

    
# create frame

frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements

frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)


# call new_game and start frame

new_game()


# always remember to check your completed program against the grading rubric
