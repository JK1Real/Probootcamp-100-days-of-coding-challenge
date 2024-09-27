from tkinter import *

# WIndow Screen
window = Tk()

window.title("My first GUI")
window.minsize(width=600,height=600)

# Labels

label = Label(text="I am a Label",font=("Arial",24,"bold"))
label.grid(row=0,column=0)
label["text"] = "Hello"

label.config(text="New Hello")

# Entry
entry = Entry()
entry.grid(row=2,column=3)


def click_button():
    print("clicked on button")
    data = entry.get()
    label.config(text=data)


button = Button(text="click",command=click_button)
button.grid(row=1,column=1)

newbutton = Button(text="dont click")
newbutton.grid(row=0,column=2)
window.mainloop()

