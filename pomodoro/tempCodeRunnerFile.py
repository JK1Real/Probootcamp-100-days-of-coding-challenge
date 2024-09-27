from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=500)
window.config(padx=100, pady=50,bg=YELLOW)


# label = Label(text="Timer",font=(FONT_NAME,24,"bold"),fg=GREEN)
# label.grid(1,2)

file = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100, 112, image=file)
canvas.create_text(100,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(2,2)

button1 = Button(text="Start")
button1.grid(3,1)

label1 = Label(text="✓",fg=GREEN)
label1.grid(4,2)

button1 = Button(text="Reset")
button1.grid(3,3)

window.mainloop()