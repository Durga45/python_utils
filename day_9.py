import time

while True:
    try:
        seconds=int(input("Enter the time in seconds: "))
        if seconds <1:
            print("Please enter a number greater than 0")
            continue
        break
    except ValueError:
        print("invalid input please enter a whole number")

print("\n timer started....")
for remaining in range(seconds,0,-1):
    mins,secs=divmod(remaining,60)
    timeFormat=f"{mins:02}:{secs:02}"
    print(f"time left :{timeFormat}",end="\r")
    time.sleep(1)

print("\n Time's up! Take a break or move on to next task.")
print("\a")