
def getFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter valid number. ")

num_people=int(input("How many people are there in group?: "))
names=[]

for i in range(num_people):
    name=input(f"Enter the name of person #{i+1}").strip()
    names.append(name)

totalBill=getFloat("enter the bill amount in number only")

share=round(totalBill/num_people,2)
print("\n "+"*"*50)
print(f"total bill: {totalBill}")
print(f"each person owes share: {share}")

for name in names:
    print(f"{name} owes {share} rupees")

print("\n"+"*"*50)