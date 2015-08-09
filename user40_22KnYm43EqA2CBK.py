#http://www.codeskulptor.org/#user40_22KnYm43EqA2CBK_0.py

import simplegui
import math

length = 500
breadth = 200
polygon_position = [length/2, breadth/2]
#Defining mouse click handler
def mouse_handler(pos):
    global polygon_position
    polygon_position = list(pos)
#Defining draw handler
def draw_handler(canvas):
    canvas.draw_polygon([[polygon_position[0]+5,polygon_position[1]-5],
                         [polygon_position[0]+5,polygon_position[1]+5],
                         [polygon_position[0]-5,polygon_position[1]+5],
                         [polygon_position[0]-5,polygon_position[1]-5]],40, 'Blue','Red')	

#Creating a frame(
frame = simplegui.create_frame("Test", length, breadth)
frame.set_canvas_background('White')

#Registering a mouse event and draw event
frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw_handler)

frame.start()