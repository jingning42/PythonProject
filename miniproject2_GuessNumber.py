# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# 我还需要加一些注释，以及优化输出：lower or large 
# 这个不容易让人明白到底是猜大了还是小了
# 另外还需要debug,输出一些错误输入的信息
# 输出提示默认范围是0-100

import simplegui
import random
import math

# initialize global variables used in your code
number_remain_guess = 7
secret_number = random.randint(0, 100)
number_n = 7
message = 'New game. Range is from 0 to 100'


# helper function to start and restart the game
def new_game():
    global number_remain_guess, secret_number, message, number_n
    number_remain_guess = number_n
    print message
    print 'Number of remaining guesses is', number_remain_guess 
    print ''
  

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    
    global number_remain_guess, secret_number, message, number_n
    secret_number = random.randint(0, 100) 
    message = 'New game. Range is from 0 to 100'
    number_n = 7
    new_game()
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    
    global number_remain_guess, secret_number, message, number_n
    secret_number = random.randint(0, 1000) 
    message = 'New game. Range is from 0 to 1000'
    number_n = 10   
    new_game()
    

###################### For more of a challenge ########################
def assignment1(x):
    global low
    low = int(x)

def assignment2(x):
    global high
    high = int(x)

def range_chanllenge():
    # button that changes range to range [low,high) and restarts
    
    global secret_number, message, number_n, low, high
    try:
        secret_number = random.randint(low, high) 
        message = 'New game. Range is from '+str(low)+' to '+str(high)
        number_n = int( math.log( high - low + 1, 2) + 1)
        new_game()
    except:
        print 'Please input your low number and high number.'
        print 'Then click Range:low-high bottun again!'
        print ''
        
########################################################################    
    
def input_guess(guess):
    # main game logic goes here	
    
    global number_remain_guess, secret_number, message
    
    guess_number = int(guess)
    number_remain_guess -= 1
    
    print 'Guess was',guess
    print 'Number of remaining guesses is',number_remain_guess
    
    if number_remain_guess > 0:
        if guess_number == secret_number:
            print 'Correct!'
            print ' '
            return new_game()
        elif guess_number > secret_number:
            print 'Higher!'
        elif guess_number < secret_number:
            print 'Lower!'
        else:
            print 'Your input is invaild.Please guess a number in range.'
        print ''
    elif number_remain_guess == 0:
        if guess_number == secret_number:
            print 'Correct!'
            return new_game()
        else: 
            print 'You ran out of guesses.  The number was',secret_number
            print ''
            new_game()

    
# create frame
frame = simplegui.create_frame("Guess the number", 300, 300)


# register event handlers for control elements
frame.add_button("New  Game", new_game, 120)
frame.add_button("Range:0-100", range100, 120)
frame.add_button("Range:0-1000", range1000, 120)
####
frame.add_button('Range:low-high',range_chanllenge, 120)
####
frame.add_input('Your Guess Number', input_guess, 100)
####
frame.add_input('Low', assignment1, 100)
frame.add_input('Hign', assignment2, 100)


# call new_game and start frame
frame.start()
new_game()

# always remember to check your completed program against the grading rubric
