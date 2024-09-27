morse={ 
        "A":".-","B":"-...","C":"-.-.","D":"-..","E":".",
        "F":"..-.","G":"--.","H":"....","I":"..","J":".---",
        "K":"-.-","L":".-..","M":"--","N":"-.","O":"---",
        "P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-",
        "V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."
        }


def text_to_morse(text):
    let=[morse[i.upper()] for i in text]
    text=' '.join(let)
    return text

def morse_to_text(text):
    let=text.split(" ")
    text=[j  for i in let for j,k in morse.items() if i==k]
    text=''.join(text)
    return text

text=input("Enter text")

print(text_to_morse(text=text))
# print(morse_to_text(text))