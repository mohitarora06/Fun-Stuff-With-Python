#http://www.codeskulptor.org/#user40_GLhT4cCQPb_4.py

# implementation of card game - Memory

import simplegui
import random

card_list= []
exposed_list= []
turns= 0
# helper function to initialize globals
def new_game():
    global card_list, exposed_list, state, turns
    card_list= []
    exposed_list= []
    for i in range(8):
        card_list.append(i)
        card_list.append(i)
    for i in range(len(card_list)):
        exposed_list.append(False)
    print exposed_list
    random.shuffle(card_list)
    turns=0
    state=0
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, card_pos1, card_pos2, turns
    card_pos= pos[0]/50
    if exposed_list[card_pos]== False:
        if state==0:
            card_pos1= card_pos
            exposed_list[card_pos]= True
            state=1
        elif state==1:
            card_pos2= card_pos
            exposed_list[card_pos]= True
            state= 2
        else:
            if card_list[card_pos1]!= card_list[card_pos2]:
                exposed_list[card_pos1]= False
                exposed_list[card_pos2]= False
                turns = turns +1
            label.set_text("Turns ="+ str(turns))   
            card_pos1= card_pos
            exposed_list[card_pos]= True
            state=1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(card_list)):
        if exposed_list[i]== False:
            canvas.draw_polygon([[50*i, 0], [(50*i)+49,0], [(50*i)+49,100], [50*i, 100]], 1, 'Red')
        else:
            canvas.draw_text(str(card_list[i]),[50*i,100], 100, "White")
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns ="+ str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric