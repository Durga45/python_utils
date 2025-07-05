#self intro script generator

import datetime

name=input("What is your name?: ").strip()
age=int(input("How old are you?: "))
city=input("Wich city do you live in?: ").strip()
profession=input("What is your Profession?: ").strip()
hobby=input("What is your hobyy?: ").strip()

intro_message=(
    f"Hello! my name is {name}, I am {age} years old and live in {city}"
    f" I work as a {profession} and I absolutely enjoy {hobby} in my free time"
    f" Nice to meet you!\n"
)

current_date=datetime.date.today().isoformat()
intro_message +=f"\n Logged on :{current_date}"

border="*"*80
final_output=f"{border}\n {intro_message}\n{border}"
print("\n"+ final_output)