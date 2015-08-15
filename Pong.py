# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0, 0]
    if direction == RIGHT:
        ball_vel[0] += random.randrange(120, 240) / 60
        ball_vel[1] -= random.randrange(60, 180) / 60
    elif direction == LEFT:
        ball_vel[0] -= random.randrange(120, 240) / 60
        ball_vel[1] += random.randrange(60, 180) / 60

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score1, score2  # these are numbers
    global score1, score2  # these are ints
    
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #Collide and reflect
    if ball_pos[0] < (BALL_RADIUS + PAD_WIDTH):
        if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -1.1 * ball_vel[0]
        else:
            score2 += 1
            spawn_ball(RIGHT)    
    elif ball_pos[0] > (WIDTH - PAD_WIDTH - BALL_RADIUS):
        if ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0]
        else:
            score1 += 1
            spawn_ball(LEFT)
    elif ball_pos[1] < BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] > HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "Orange")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos - paddle1_vel - HALF_PAD_HEIGHT <= 0 and paddle1_pos + paddle1_vel + HALF_PAD_HEIGHT >= HEIGHT:
        paddle1_pos += 0
    else:
        paddle1_pos += paddle1_vel
    if paddle2_pos - HALF_PAD_HEIGHT <= 0 and paddle2_pos + HALF_PAD_HEIGHT >= HEIGHT:
        paddle2_pos += 0
    else:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, (paddle1_pos + HALF_PAD_HEIGHT)],
                     [HALF_PAD_WIDTH, (paddle1_pos - HALF_PAD_HEIGHT)], 
                     PAD_WIDTH, "Black")
    
    canvas.draw_line([(WIDTH - HALF_PAD_WIDTH), (paddle2_pos + HALF_PAD_HEIGHT)],
                     [(WIDTH - HALF_PAD_WIDTH), (paddle2_pos - HALF_PAD_HEIGHT)], 
                     PAD_WIDTH, "Red")
    
    # draw scores
    canvas.draw_text("Score Left: " + str(score1), [50, 30], 30, 'White')
    canvas.draw_text("Score Right: " + str(score2), [350, 30], 30, 'White')
    
def button_handler():
    new_game()
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 4
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel = -acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = +acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = +acc
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = 0
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel = +acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = -acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = +acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = -acc

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background('Green')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", button_handler, 100)


# start frame
new_game()
frame.start()
