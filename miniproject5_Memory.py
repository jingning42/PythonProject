# Game: Memory
# wiki: http://en.wikipedia.org/wiki/Concentration_(game)
# @auther: JING-TIME / Jenny Zhang
# e-mail: changchongning@gmail.com
# version: 2.0
# update: 2014.5.4

import simplegui
import random

WIDTH = 800
HEIGHT = 100
my_list = range(1,9) + range(1,9)

# helper function to initialize globals
def new_game():
    global my_list, Turns, exposed, state
    Turns = 0
    state = 0
    exposed = [False for i in range(16)]            # or exposed = [False] * 16
    random.shuffle(my_list)
    label.set_text('Turns = ' + str(Turns))
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global my_list, Turns, exposed, state, num1, num2
    num = pos[0]//50
    if not exposed[num]:
        exposed[num] = True
        if state == 0:
            state = 1
            Turns += 1
            num1 = pos[0]//50 
        elif state == 1:
            num2 = pos[0]//50
            state = 2
        else:
            if my_list[num1] != my_list[num2]:
                exposed[num1] = False
                exposed[num2] = False
            state = 1
            Turns += 1
            num1 = pos[0]//50               
    label.set_text('Turns = ' + str(Turns))
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global my_list, Turns, exposed
    for i in range(16):
        canvas.draw_text(str(my_list[i]), (10 + i*WIDTH/16, 70), 60, 'White')
        if not exposed[i]:
            canvas.draw_line((50*i+25, HEIGHT), (50*i+25, 0), WIDTH/16-0.75, 'Green')
                       
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# sound
sound = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg')
sound.set_volume(0.5)
sound.play()

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric