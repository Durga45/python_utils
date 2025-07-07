def calculateMinutes(age_years):
    days_in_year = 365.25
    hours_in_day = 24
    minutes_in_hour = 60

    total_days = age_years * days_in_year
    total_hours = total_days * hours_in_day
    total_minutes = total_hours * minutes_in_hour

    return round(total_days), round(total_hours), round(total_minutes)


while True:
    try:
        age = float(input("Enter your age in years: "))
        
        if age < 0:
            print("Age can't be negative. Try again.\n")
            continue
        
        days, hours, minutes = calculateMinutes(age)
        
        print("\nYou are approximately:")
        print(f" - {days} days old")
        print(f" - {hours} hours old")
        print(f" - {minutes} minutes old\n")

        again = input("Would you like to try again? (y/n): ").strip().lower()
        if again != 'y':
            print("\nGoodbye! 👋")
            break

    except ValueError:
        print("Please enter a valid number for age.\n")
