import smtplib

def send_quotes(quote):
    my_email ="thisisnotallowed384@gmail.com"
    my_password = "mejj afih zkul vfgg"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # Make this connection secure 


        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="secondname@myyahoo.com",msg=f"subject:New\n\n{quote}")


import datetime as dt

import random

def quote_worker():
    with open(file="quotes.txt",mode="r") as file:
        data = file.readlines() 

    now = dt.datetime.now()
    year = now.year
    month = now.month
    day_of_the_year = now.day

    date_of_birth = dt.datetime(year=1995,month=12,day=26)
    quote = random.choice(data)

    birthday_day = date_of_birth.strftime("%A")
    current_day = now.strftime("%A")

    print(quote)
    print(date_of_birth.strftime("%A"))
    print(now.strftime("%A"))

    if birthday_day== current_day:
        send_quotes(quote=quote)

    
quote_worker()



