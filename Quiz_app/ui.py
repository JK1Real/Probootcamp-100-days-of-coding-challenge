from tkinter import *
import time
THEME_COLOR = "#375362"

class Quiz_interface():
    def __init__(self) -> None:
        self.i = 0
        self.score=0
        self.questions = None
        self.answers = None
    def check(self,questions,anwsers) -> None:
        self.questions = questions
        self.answers = anwsers
        self.window = Tk()
        self.window.config(background="black")
        self.window.minsize(width=500,height=500)

        label_score = Label(text="Score",fg="White",background="black")
        label_score.grid(row=1,column=3)

        self.canvas = Canvas(height=250,width=400)
        self.question_change = self.canvas.create_text(200,100,font=("Arial",10,"italic"),fill="black",text=self.questions[self.i], width= 200)
        
        self.canvas.grid(row=2,column=2)

        green_image = PhotoImage(file="./images/true.png")
        green_button = Button(image=green_image,command=self.check_answer_right)
        green_button.grid(row=3,column=1)
        
        red_image = PhotoImage(file="./images/false.png")
        red_button = Button(image=red_image,command=self.check_answer_wrong)
        red_button.grid(row=3,column=3)

        self.window.title("Quiz")
        self.window.mainloop()

    def check_answer_right(self):
        print(self.i)
        print(self.questions[self.i])
        anw = self.answers[self.i]
        print(anw)
        if anw:
            print("True works")
            self.canvas.config(background="green")     
            self.score+=1

        else :
             self.canvas.config(background="red")
        self.i+=1
        self.canvas.after(1000,self.update_canvas)


    def check_answer_wrong(self):
            print(self.i)
            print(self.questions[self.i])
            anws = self.answers[self.i]
            print(anws)
            if  anws:
                self.canvas.config(background="red")
            else:
                print("False works")
                self.canvas.config(background="green")     
                self.score+=1
            self.i+=1
            self.canvas.after(1000,self.update_canvas)
            
            

    def update_canvas(self):
        self.canvas.config(background="white")
        self.canvas.itemconfig(self.question_change,text=self.questions[self.i])