
import tkinter
from my_turtle_funtcions import *
from my_turtle_funtcions import t
import turtle
from winner import winner
import random


window=tkinter.Tk()

canvas = tkinter.Canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')



tu=turtle.RawTurtle(canvas)
tu.forward(100)
click_tur_list=[]
click_pos=[(-50,150),(50,150),(150,150),
            (-50,50),(50,50),(150,50),
            (-50,-50),(50,-50),(150,-50),(150,-50)]

# Function i made inside my_turtle_funtions() module passes the t object for borders
t=turtles_forward(300,'red',canvas=canvas)

def stop_game():
    """Unbind turtle click events to stop further interactions."""
    global click_tur_list
    for tur in click_tur_list:
        tur.onclick(None)  # Unbind the click event for each turtle
    print("Game Over. No more clicks allowed.")
 

def heading(color):
    turn=turtle.RawTurtle(canvas)
    turn.hideturtle()
    turn.goto(x=-100,y=180)
    if color=="red":
        turn.pencolor("Red")
        turn.write('Reds Turn',font=('arial',50,'bold'), align='left')
        # Delay before clearing the text
        canvas.after(1000, turn.clear)  # Delay of 1000ms (1 second)
    elif color=="blue":
        turn.pencolor("Blue")
        turn.write('Blues Turn',font=('arial',50,'bold'), align='left')
        canvas.after(1000,turn.clear)
    
def player_click(tur):
    tur.click_count+=1  
    print(f"Click Number: {tur.click_count}")
    global t
    print(t[0].pencolor())
    if t[0].pencolor()=="red" and tur.click_count==1:
        
        tur.pencolor("red")
        tur.write('x',font=('arial',30,'bold'), align='left')
        result,winning_turtle=winner(tur=tur,color="red",canvas=canvas)  
        print(result)
        # Function i made inside my_turtle_funtions() module
        if result=="pass":
            heading("blue")
            t = turtles_forward(300,'blue',canvas=canvas)
            click_tur_list.remove(tur)
            ran=random.choice(click_tur_list)
            player_click(ran)
        if result=="blue"or result=="red":
            stop_game()
            winning_turtle.write(f"{result} wins",font=('arial', 50, 'normal'))
        
    elif t[0].pencolor()=="blue"and tur.click_count==1:
        
        tur.pencolor("blue")
        tur.write('x',font=('arial',30,'bold'), align='left')
        result,winning_turtle=winner(tur=tur,color="blue",canvas=canvas)
        print(result) 
        if result=="pass":
            heading("red")
            
            t=turtles_forward(300,'red',canvas=canvas)
        # tur.write('x',font=('arial',30,'bold'), align='left')
        click_tur_list.remove(tur)
        if result=="blue"or result=="red":
            stop_game()
            winning_turtle.write(f"{result} wins",font=('arial', 50, 'normal'))


heading("red")
for i,j in click_pos:
        tur=turtle.RawTurtle(canvas)
        tur.shape('square')
        tur.shapesize(4)
        tur.penup()
        tur.speed(10)
        tur.setpos(i,j)
        tur.pendown()
        tur.click_count=0
        tur.onclick(lambda x,y,t=tur:player_click(tur=t))
        
        click_tur_list.append(tur)



    
# click_tur_list[0].write("X",font=('arial',25,'bold'), align='center')


window.mainloop()
