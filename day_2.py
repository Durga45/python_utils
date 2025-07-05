#bio generator for instagaram

import textwrap

name=input("Enter your name: ").strip()
profession=input("Enter your profession: ").strip()
passion=input("Enter your passion: ").strip()
emoji=input("Enter your emoji: ").strip()
website=input("Enter your website: ").strip()

print("\n Choose your style: ")
print("1. simple lines")
print("2. vertical flair")
print("3. emoji sandwich")

style=int(input("enter 1 ,2 or 3: "))

def generateBio(style):
    if style==1:
        return f"{emoji} {name} | {profession} \n @@ {passion }\n {website}"
    elif style==2:
        return f"{emoji} {name} \n {profession} (.)_(.) \n {passion} \n {website} <==>"
    elif style==3:
        return f"{emoji*3}\n {name} -{profession}\n {passion} ==>\n {website} <==^==>"
    else:
        return "enter only 1 ,2 or 3"
    

bio=generateBio(style)
print("\n your stylish bio :\n")
print("*"*50)
print(textwrap.dedent(bio))
print("*"*50)

save=input("do you want to sace this bio? (y/n)")

if save=='y':
    filename=f"{name.lower().replace(' ',"_")}_bio.txt"
    with open (filename,'w',encoding="utf-8") as f:
        f.write(bio)
    print("file saved")
    