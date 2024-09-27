import datetime as dt



Time = dt.time(minute=0, second=0)
second=0

def label_time(window,label,entry):
    global Time,second
    
    if Time.second==59:
        Time=Time.replace(minute=1,second=0)
        label.config(text=Time.strftime("%M:%S"), font=("Helvetica", 30))
        entry.config(state="disabled")
        entry.bind("<Key>", lambda e: "break") 
    
        return 0
    else:
        second+=1
        Time=Time.replace(second=second)

    window.after(1000,lambda x=window,y=label,entry=entry:label_time(x,y,entry))
    label.config(text=Time.strftime("%M:%S"), font=("Helvetica", 30))
        
        
        
    