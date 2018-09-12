import random
import string

def pass_gen(level):
    lenght= int(input("Enter password lenght: "))

    l= string.ascii_lowercase
    u = string.ascii_uppercase
    s = string.punctuation
    d = string.digits

    strong = "".join([random.choice(l+u+s+d) for i in range(lenght)])
    medium = "".join([random.choice(l+u+d) for i in range(lenght)])
    low = "".join([random.choice(l+d) for i in range(lenght)])

    if level=="strong":
        return(strong)
    elif level=="medium":
        return(medium)
    elif level=="low":
        return (low)

selection = input("Select an encription level: 'strong', 'medium' or 'low':  ")
if selection== "strong":
    print(pass_gen(level="strong"))
elif selection== "medium":
    print(pass_gen(level="medium"))
elif selection =="low":
    warning=input("WARNING!!! Low encription is not recomended!\n Do you realy want to contune? y/n ")
    if warning == ('y'):
        warning= print(pass_gen(level="low"))
    else:
        warning ==("n")
        exit

else:
    if selection !=("strong","medium","long"):
        print("Error!!! Plese enter: 'strong', 'medium' or 'low'  ")
#print(pass_gen(selection))
