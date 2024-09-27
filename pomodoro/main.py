from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(time_text,text="0:00")
    label1.config(text="",fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps%8==0:
        label.config(text="Long Break",fg=RED)
        count_down(long_break_sec)
    elif reps%2==0:
        label.config(text="Short Break",fg=PINK)
        count_down(short_break_sec)
    else:
        count_down(work_sec)

        label.config(text="Work",fg=GREEN) 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_min==0 and count_sec<10:
        count_sec = "0"+str(count_sec) 
    canvas.itemconfig(time_text,text=f"{count_min}:{count_sec}")
    if count>0 :
        global timer 
        timer = window.after(1000,count_down,count-1)
    else :
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✓"
            label1.config(text=marks,fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=500)

label = Label(text="Timer",bg=YELLOW,font=(FONT_NAME,34,"bold"),fg=GREEN)
label.grid(row=1,column=2)

file = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100, 112, image=file)
time_text = canvas.create_text(100,112,text="0:00",fill="white",font=(FONT_NAME,25,"bold"))
window.config(padx=100, pady=50,bg=YELLOW)

canvas.grid(row=2,column=2)

button1 = Button(text="Start",command=start_timer)
button1.grid(row=3,column=1)

label1 = Label(fg=GREEN,font=(FONT_NAME,35,"bold"))
label1.grid(row=4,column=2)

button1 = Button(text="Reset",command=reset_timer)
button1.grid(row=3,column=3)

window.mainloop()