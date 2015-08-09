# template for "Stopwatch: The Game"
import simplegui
# define global variables
value = 0
game = False
x = 0
y = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = 0
    seconds = 0
    milli = 0
    
    minutes = t / 600
    seconds_temp = t % 600
    seconds = seconds_temp / 10
    milli = seconds_temp % 10
    if seconds >= 10:
        return str(minutes) + ":" + str(seconds) + "." + str(milli)
    else:
        return str(minutes) + ":0" + str(seconds) + "." + str(milli)
   
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global game
    timer.start()
    game = True
    
def stop_handler():
    global game, y, x, value 
    timer.stop()
    if game:
        game = False
        y += 1
        time = format(value)
        if time[-1] == "0":
            x += 1
            
def reset_handler():
    global value, x, y
    timer.stop()
    value = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global value 
    value += 1
    
# define draw handler
def draw_handler(canvas):
    global value, x, y
    canvas.draw_text(format(value), [115, 115], 40, "White")
    canvas.draw_text(str(x) + "/" + str(y), [250, 30], 30, "Green")
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_handler, 100)
frame.add_button("Stop", stop_handler, 100)
frame.add_button("Reset", reset_handler, 100)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()


# Please remember to review the grading rubric
