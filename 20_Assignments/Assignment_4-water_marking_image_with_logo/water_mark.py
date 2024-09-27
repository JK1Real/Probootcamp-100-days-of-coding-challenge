# Todo1- Using Tkinter make the box for dragging image and box for adding text
#Todo2-use the text to water mark the image

import tkinter as tk
from PIL import ImageGrab,ImageTk,ImageFont,ImageDraw

# Window where everything is shown like button image etc
Window=tk.Tk()
Window.minsize(height=500,width=500)

# Text box where we enter the text
enter=tk.Entry()
enter.place(x=0)

#This function gets the text entered in above textbox when we click the button created below and shows it
def com():
    global text
    text=enter.get()
    print(text)
    lab=tk.Label(text=text)
    lab.place(y=40)

# Creeated button where when click on it shows the text which was entered on enter textbox
button=tk.Button(text="Submit",command=com)
button.place(y=20)


lab=tk.Label(Window)
lab.place(y=90)

def clip_board():
    global lab
    lab.option_clear()
    global clip
    clip=ImageGrab.grabclipboard()
    if clip is None or type(clip)==str:
        lab=tk.Label(text="There is no image in your clipboard")
        lab.place(y=90)
    else: 
        newsize=(300,300)
        clip.resize(newsize)
        image=ImageTk.PhotoImage(clip)
    
        print(type(image))
        
    
        lab.image=image
        lab.config(image=image)

button=tk.Button(text="Clipboard",command=clip_board)
button.place(y=70)

def combine_text_with_clipboard():
    global clip
    global text
    print(type(clip))
    print(text)
    newsize=(300,300)
    clip.resize(newsize)
    clip=ImageTk.PhotoImage(clip)
    image=ImageTk.getimage(clip)
    print(type(image))
        
    draw=ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=50)
    text_color = (255, 0, 255)  
    position = (100, 0)

    draw.text(position,text,fill=text_color,font=font)
    image=ImageTk.PhotoImage(image)
    cliplabel=tk.Label(image=image)
    cliplabel.place(y=295)
    cliplabel.image=image
    cliplabel.config(image=image)
    

button=tk.Button(text="Clipboardwithtext",command=combine_text_with_clipboard)
button.place(y=270)


Window.mainloop()

