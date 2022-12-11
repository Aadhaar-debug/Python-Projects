# This program determines how much age are we left with
# new project made  aadhaar koul
age = input("Enter your age")
age_as_int = int (age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days {weeks_remaining} weeks and {years_remaining} years ahead of you !!!! ")
