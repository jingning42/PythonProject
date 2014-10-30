########################################################################### 
#                           Stopwatch: The Game                           #
###########################################################################
# Game Rules                                                              #
# click 'start' button and the time will begin                            #
# click 'stop' button, if time is on a whole second you will get a score  #
# click 'reset' button to reset the current time to zero                  #
###########################################################################
#--userscript--	 				                                  		  #
#@author: sinaweibo@JING-TIME											  #
#@version: 2.1															  #
#@update: 2014.4.22                                                       #
###########################################################################
#
import simplegui
# define global variables
time = 0
scores = 0
tries = 0
Boolean = True
massage1 = "click Start to play game"
massage2 = "click Stop on a whole second" 
massage3 = "    and you will get a score "
massage4 = "click Reset to play new game"
massage5 = "click Help to close this page"


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = 0
    B = 0
    C = 0
    D = 0
    if t < 6000:
        A = t / 600
        B = (t / 100) % 6
        C = (t % 100)/ 10 
        D = t % 10  
    else:
        A = 9
        B = 5
        C = 9
        D = 9
        timer.stop()
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)
    
# define the feedback function
def feedback():
    global scores, tries
    return str(scores) +'/'+ str(tries)

# define event handlers for buttons; "Start", "Stop", "Reset", "Help"
def start_game():
    if time < 6000:
        timer.start()
           
def stop_game():
    global time, scores, tries
    if timer.is_running():
        tries += 1
        if time % 10 == 0:
            scores += 1
        timer.stop()
    
def reset_game():
    timer.stop()
    global time, scores, tries
    time = 0
    scores = 0
    tries = 0

def game_rule():
    timer.stop()
    global Boolean
    Boolean = not(Boolean)
    
# define event handler for timer with 0.1 sec interval
def event():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(feedback(), [168,32], 30, 'Red')
    if Boolean:
        if time < 6000:
            canvas.draw_text(format(time), [70,115], 40, 'White')
        else:
            canvas.draw_text('Game Over', [42,115], 40, 'White')
    else:
        canvas.draw_text(massage1, [13,70], 15, 'White')
        canvas.draw_text(massage2, [13,90], 15, 'White')
        canvas.draw_text(massage3, [13,110], 15, 'White')
        canvas.draw_text(massage4, [13,130], 15, 'White')
        canvas.draw_text(massage5, [13,150], 15, 'White')
       
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game',250,200)

# register event handlers
frame.add_button('Start', start_game ,80)
frame.add_button('Stop', stop_game ,80)
frame.add_button('Reset', reset_game ,80)
frame.add_button('Help', game_rule ,80)

timer = simplegui.create_timer(100, event)
frame.set_draw_handler(draw_handler)


# start frame
frame.start()


# Please remember to review the grading rubric