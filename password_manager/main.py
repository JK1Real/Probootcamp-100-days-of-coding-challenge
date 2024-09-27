from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for char in range(nr_letters) ]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters+password_numbers+password_symbols 
    random.shuffle(password_list)

    password = "".join(password_list)
    passwordentry.insert(index=0,string=password)
    passwordentry.clipboard_append(string=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = websiteentry.get()
    email = emailentry.get()
    password = passwordentry.get()

    new_data = {
        website:{
            "email":email,
            "password":password
        }
            }

    if len(website)==0 or len(email)==0 or len(password) ==0:
        messagebox.showinfo(title="Oops",message="Please dont leave any fields empty")
    else:
        try:
            with open("data.json",'r',encoding="utf-8") as file:
                # Reading the old data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json",'w',encoding="utf-8") as file:
            # Saving the updated data
                json.dump(new_data, file,indent=4)
        else:
            with open("data.json",'w',encoding="utf-8") as file:
                # Saving the updated data
                json.dump(data, file,indent=4)
                
        finally:
            websiteentry.delete(0,END)
            passwordentry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    try:
        website = websiteentry.get()
        with open("data.json","r") as file:
            data = json.load(file)
    except KeyError:
            messagebox.showinfo(title="Error",message="websites  details data  doesnt exists ")
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="websites  details data  doesnt exists ")
    else:
         messagebox.showinfo(title=website,message=f"Website :{website}\nEmail: {data[website]['email']}\nPassword : {data[website]['password']}")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password manager")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

file = "logo.png"
canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_img = PhotoImage(file=file)
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#labels
website = Label(text="Website:")
website.grid(row=1,column=0)
email = Label(text=  "Email/Username:")
email.grid(row=2,column=0)
password = Label(text="Password:")
password.grid(row=3,column=0)


#entries
websiteentry = Entry(width=32)
websiteentry.focus()
websiteentry.grid(row=1,column=1)
emailentry = Entry(width=50)
emailentry.insert(index=0,string= "jeromk60@gmail.com")
emailentry.grid(row=2,column=1,columnspan=2)

passwordentry = Entry(width=32)
passwordentry.grid(row=3,column=1)

#buttons

passwordgeneration = Button(text="Generate Password",command=password_generator,width=14)
passwordgeneration.grid(row=3,column=2)

add = Button(text="Add",width=36,command=save)
add.grid(row=4,column=1,columnspan=2)

search = Button(text="Search",command=search,width=14)
search.grid(row=1,column=2)

window.mainloop()