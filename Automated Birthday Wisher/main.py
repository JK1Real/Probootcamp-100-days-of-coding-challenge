##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
from email.message import EmailMessage
import pandas as pd
import datetime as dt
import regex as re
import random

email = "thisisnotallowed384@gmail.com"
password = "cxmv ppoi mlmv bmxd"

def send_letter(letter):
    msg = EmailMessage()
    msg["subject"] = "Happy Birthday"
    msg["From"] = email
    msg["to"] = "secondname@myyahoo.com"
    msg.set_content(letter)

    with  smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=email,password=password)
        connection.send_message(msg)



def birth_day_letter():
    list_of_letters = ["letter_1.txt","letter_2.txt","letter_3.txt"]

    birth_data = pd.read_csv("birthdays.csv")
    for i in  range(0,len(birth_data)):
        now = dt.datetime.now()
        now_year = now.year
        now_month = now.month
        now_day = now.day

        birth_name = birth_data.loc[i]["name"]
        birth_day = int(birth_data.loc[i]["day"])
        birth_month = int(birth_data.loc[i]["month"])

        if now_day==birth_day and now_month == birth_month:
            choice_letter = random.choice([0,1,2])
            with open(f"./letter_templates/{list_of_letters[choice_letter]}","r") as letter:
                data = letter.read()
                print(data)
                pattern =re.compile(r"\W\w+\W")
                new_data = re.sub(pattern,birth_name,data,count=1)
                print(new_data)
                send_letter(new_data)

birth_day_letter()