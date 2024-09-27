import turtle

positions=[(0,200),(100,200),
           (-100,100),(-100,0)]

t=[]
def turtles_change_pencolor(color):
    for tur in t:
        tur.pencolor(color)

def turtles_forward(distance,color,canvas):
    global t
    t=[]
    # To make the turtles starting position in 4 places
    for i,j in positions:
        tur=turtle.RawTurtle(canvas=canvas)
        tur.pensize(15)
        tur.penup()
        tur.speed(10)
        tur.setpos(i,j)
        tur.pendown()
        t.append(tur)
    for tur in t[:2]:
        tur.right(90)
    turtles_change_pencolor(color)
    for tur in t:
        tur.hideturtle()
        tur.speed(10)
        tur.forward(distance)
    return t






