import turtle

red=[]
blue=[]



def winner_turtle(color,winner_list,comb,canvas):
    winning_turtle=turtle.RawTurtle(canvas)
    winning_turtle.hideturtle()
    winning_turtle.pensize(50) 
    winning_turtle.pencolor(color)

    winning_turtle.penup()
    winning_turtle.goto(winner_list[comb[-1]])
    
    winning_turtle.pendown()
    winning_turtle.goto(winner_list[comb[0]])
    winning_turtle.penup()
    winning_turtle.goto(x=-50,y=50)
    
    winning_turtle.pencolor("white")
    winning_turtle.pensize(50)
    return winning_turtle
    
    
def winner(tur,color,canvas):
    global blue
    global red
    # Check for winning combinations
    winning_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal from top-left to bottom-right
        [2, 4, 6]   # Diagonal from top-right to bottom-left
    ]
    winner_list=[(-50,150),(50,150),(150,150),
            (-50,50),(50,50),(150,50),
            (-50,-50),(50,-50),(150,-50)]
    pos=tur.pos()
    if color=="red":
        red.append(winner_list.index(pos))
    if color=="blue":
        blue.append(winner_list.index(pos))

    for comb in winning_combinations:
        if all(pos in red for pos in comb):
            winnig_turtle=winner_turtle(color="red",canvas=canvas,winner_list=winner_list,comb=comb)           
            print("Red wins!")
            return "red",winnig_turtle
            
        elif all(pos in blue for pos in comb):
            winnig_turtle=winner_turtle(color="blue",canvas=canvas,winner_list=winner_list,comb=comb)    
            print("Blue wins!")
            return "blue",winnig_turtle
    else:
        return "pass",0
