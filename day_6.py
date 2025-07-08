import datetime


entry=input("What did you learned today: ").strip()

rating=input("Rate your productivity today(1-5): ").strip()

now=datetime.datetime.now()
date_str=now.strftime("%Y-%m-%d - %I:%M %p")

journal_entry=f"\n date: {date_str} \n {entry}"

if rating:
    journal_entry +=f"\n productivity rating: {rating}\n"
journal_entry+="\n"+"-"*50

with open("learningjournal.txt","a",encoding="utf-8") as f:
    f.write(journal_entry)

print(f"\n your journal entry has benn saved to 'learningsjournal.txt' file.")
