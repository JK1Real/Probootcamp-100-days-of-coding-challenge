import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States game")

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)

i=0
states_guessed_by_user = []
game_is_on = True
while  game_is_on:
    title = f"Guess the name {i}/50"
    state_user_typed = turtle.textinput(title= title, prompt="Whats another states name?")
    state_user_typed = state_user_typed.title()
    print(state_user_typed)
    state_data = pd.read_csv("50_states.csv")
    states = state_data["state"].to_list()
    if state_user_typed in state_data["state"].to_list()  :
        coors = state_data[state_data["state"]== state_user_typed].iloc[0].to_list()[1:]
        states_guessed_by_user.append(state_user_typed)
        print(coors)
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(coors)
        pen.write(state_user_typed,font=("Arial", 8, "normal"))
        i = i+1
    if i >50 or state_user_typed == "Exit":
            for state in states_guessed_by_user:
                 if state in states:
                      states.remove(state)
            learn = pd.DataFrame({"state":states})
            learn.to_csv("states_to_learn.csv")                  
            print(states)
            game_is_on = False
            
            
pen.onscreenclick(get_mouse_click_coor)
pen.mainloop()
