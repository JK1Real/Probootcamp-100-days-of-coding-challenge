import tkinter as tk
from test import label_time
import datetime as dt


window=tk.Tk()
window.minsize(width=1000,height=300)

string="""In today's fast-paced digital world, typing has become a crucial skill.
Whether you're writing an email, coding, or simply chatting online,
your ability to type efficiently can save you time and effort.
Practice is essential to improve your typing speed and accuracy.
By focusing on both form and function, you can gradually build muscle memory and reduce errors. 
The key is to maintain a steady rhythm and minimize unnecessary movements.
Over time, you'll notice a significant improvement in your ability to type faster without sacrificing precision.
Keep practicing and stay consistent.
"""
txt=string.split("\n")[:-1]

text=tk.Text(window,width=100,height=12)

text.insert(tk.INSERT,string)
text.place(x=10,y=30)
text.config(state="disabled")

Time = dt.time(minute=0, second=0)
second=0

label=tk.Label(window,text=Time.strftime("%M:%S"), font=("Helvetica", 30))
label.place(x=500,y=180)


line=0    
start_index=f"{str(line+1)}.0"
end_index="1.1"
value=1
prev_char=""
typed_texts_no=0
txt_length=len(txt[line])
correctness=0
wrongness=0
accurate_score="0 %"
prev_line_value=0


wrongness_label=tk.Label(window,width=10,text=f"Wrong:{wrongness}",fg="red",font=("Helvetica", 12))
wrongness_label.place(x=500)

correctness_label=tk.Label(window,width=10,text=f"Correct:{correctness}",fg="green",font=("Helvetica", 12))
correctness_label.place(x=600)

accuracy_score=tk.Label(window,width=20,text=f"Accuracy_score:{accurate_score}",font=("Helvetica", 12))
accuracy_score.place(x=700)

def fromentrytolabel(e,word_enrty):
        

    global start_index,end_index,value,prev_char,line,typed_texts_no,txt_length,correctness,wrongness,wrongness_label,correctness_label,accuracy_score
    
    
    def when_keyboard_equal_to_character_in_string():
            global start_index,end_index,value,prev_char,line,typed_texts_no,txt_length,window,label,correctness,string,accuracy_score,prev_line_value
            prev_char=e.char
            typed_texts_no+=1
            accuracy_score.config(text=f"Accuracy_score: {correctness/len(string) * 100:.2f}%")

            if typed_texts_no==1:
                label_time(window=window,label=label,entry=word_enrty)
                
        
            if typed_texts_no==txt_length :
                
                
                text.tag_add("tag1",start_index,end_index)
                text.tag_config("tag1",foreground="green")

                prev_line_value=value
                
                line=line+1
                txt_length=txt_length+len(txt[line])
                value=0
                start_index=f"{str(line+1)}.{value}"
                
                start_index=start_index.split(".")[0]+"."+str(value)
                end_index=start_index.split(".")[0]+"."+str(value+1)

                value=1

                return 0
        
            

        
            text.tag_add("tag1",start_index,end_index)
            text.tag_config("tag1",foreground="green")

            start_index=start_index.split(".")[0]+"."+str(value)
            end_index=start_index.split(".")[0]+"."+str(value+1)

            
        
            value=value+1
            
            return 0  
    
    def when_keyboard_not_equal_to_character_in_string():
        global start_index,end_index,value,prev_char,line,typed_texts_no,txt_length,correctness,accuracy_score,string,prev_line_value
        
        prev_char=e.char
        typed_texts_no+=1

        
        accuracy_score.config(text=f"Accuracy_score: {correctness/len(string) * 100:.2f}%")
        if typed_texts_no==1:
                label_time(window=window,label=label,entry=word_enrty)
                
           
        if typed_texts_no==txt_length:
        
                text.tag_add("tag2",start_index,end_index)
                text.tag_config("tag2",foreground="red")

                prev_line_value=value 
                line=line+1
                txt_length=txt_length+len(txt[line])
                value=0
                start_index=f"{str(line+1)}.{value}"
                
                start_index=start_index.split(".")[0]+"."+str(value)
                end_index=start_index.split(".")[0]+"."+str(value+1)
                value=1
                
                           
                return 0
        
        text.tag_add("tag2",start_index,end_index)
        text.tag_config("tag2",foreground="red")
        
        
        start_index=start_index.split(".")[0]+"."+str(value)
        end_index=start_index.split(".")[0]+"."+str(value+1)

        
        
        
        value=value+1

        return 0
    
    if e.keycode==16:# Keycode for shift key
        return 0

    # Uses when backspace is pressed 
    if e.char=='\x08' :  # This  is '\x08'-Backspace
        
        #on pressing backspace check if press is equal to '\x08'
        if value==1 and line>0:
             value=prev_line_value
             typed_texts_no=typed_texts_no-1
             line=line-1
             txt_length=typed_texts_no+1


             start_index=f"{str(line+1)}.{value}"
             start_index=start_index.split(".")[0]+"."+str(value-1)
             end_index=start_index.split(".")[0]+"."+str(value)
        
             text.tag_remove("tag1",start_index,end_index)
             text.tag_remove("tag2",start_index,end_index)
            # text.tag_config("tag1",foreground="black")
             return 0

        if value>1:
            value=value-1 #helps start index and end index to go one step back
            typed_texts_no=typed_texts_no-1

            start_index=start_index.split(".")[0]+"."+str(value-1)
            end_index=start_index.split(".")[0]+"."+str(value)
        
            text.tag_remove("tag1",start_index,end_index)
            text.tag_remove("tag2",start_index,end_index)
        # text.tag_config("tag1",foreground="black")
        return 0
    # When character typed in keyboard is equal to character in string

    if txt[line][int(start_index.split(".")[-1])]==e.char:
        correctness+=1
        correctness_label.config(text=f"Correct:{correctness}")
        when_keyboard_equal_to_character_in_string()
        return 0

    # When character typed in keyboard is not equal to character in string
    if txt[line][int(start_index.split(".")[-1])]!=e.char:
        wrongness+=1
        wrongness_label.config(text=f"Wrong:{wrongness}")
        when_keyboard_not_equal_to_character_in_string()
        return 0

# To enter words
worlds_entry=tk.Entry()
worlds_entry.place(x=20,y=220)

typing_text=worlds_entry.get()
worlds_entry.bind("<KeyPress>",lambda e, word_entry=worlds_entry:fromentrytolabel(e,word_entry))

window.mainloop()