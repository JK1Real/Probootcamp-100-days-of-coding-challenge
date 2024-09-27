from tkinter import *
import pandas as pd
from random import choice
import time


BACKGROUND_COLOR = "#B1DDC6"





current_card = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card =   choice(to_learn)
    canvas.itemconfig(image,image=card_front)
    canvas.itemconfig(card_title,text = "French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    flip_timer = window.after(1000,func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(image,image=card_back)
    canvas.itemconfig(card_title,text = "English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")


def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)

window = Tk()
window.title(string="Flashy")
window.configure(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(ms=2500,func=flip_card)
#images
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")  


canvas = Canvas(width=800,height=526)
image = canvas.create_image(400,263,image = card_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
card_title = canvas.create_text(400,158,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"italic"))

#Buttons
right_button = Button(image=right,width=50,height=50,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

wrong_button = Button(image=wrong,width=50,height=50,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

next_card()

window.mainloop()