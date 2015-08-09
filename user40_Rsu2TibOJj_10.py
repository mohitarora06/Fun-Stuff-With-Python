#http://www.codeskulptor.org/#user40_Rsu2TibOJj_11.py

import simplegui

#defining list
task= []

#defining input_text handler
def input_text(text):
    task.append(text)
    
#defining removal from list
def remove_text(text):
    if(text in task):
        task.remove(text)

#defining for removal from list using number
def removing_number(text):
    pos= int(text)
    if(pos>0 and pos<= len(task)):
        task.pop(pos-1)
#defining draw handler
def display_text(canvas):
    n=1
    for text in task:
        vertical_point= 20*n
        canvas.draw_text(str(n)+':'+text, (10,vertical_point), 20, "Gray", "monospace")
        n +=1

#defining button handler
def clear_data():
    input.set_text('')
#Setting up the frame
frame= simplegui.create_frame("List Test", 500, 200)
frame.set_canvas_background("Black")

#Adding text to the frame through text box named Task
input= frame.add_input("Task", input_text, 200)
#Removing text from the list
frame.add_input("Remove Task", remove_text, 200)
#Removing text using number
frame.add_input("Remove Text Using number", removing_number, 200)

#diplaying on the frame
frame.set_draw_handler(display_text)

#Adding button 
frame.add_button("Clear", clear_data)

#Starting frame
frame.start()