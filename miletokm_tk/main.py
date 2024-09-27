from tkinter import *


window = Tk()
window.title("Mile to Km converter")
window.minsize(height=500,width=500)

# Enrty
entry = Entry(width=7)
entry.grid(row=3,column=5,padx=20,pady=20)

# Label
label = Label(text="Miles")
label.grid(row=3,column=6)

label1 = Label(text="is equal to ")
label1.grid(row=4,column=5)


ans = Label(text=0)
ans.grid(row=4,column=6)

label2 = Label(text="kms ")
label2.grid(row=4,column=7)

# Button
def calculate():
    data = int(entry.get())
    data = data * 1.60934
    ans.config(text=data)

button = Button(text="Calculate",command=calculate)
button.grid(row=5,column=6)

window.mainloop()