#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


import re
with open(file="Input/Letters/starting_letter.txt",mode="r") as file:
    content = file.read()
    print(content)

with open(file="Input/Names/invited_names.txt",mode="r") as file:
    names = file.readlines()
    

for name in names:
    with open(file=f"Output/{name.strip()}.txt",mode="w") as file:
        file.write(content.replace("[name]",name.strip()))

