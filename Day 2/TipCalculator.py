# Project 2

print("Welcome to the Tip Calculator!")
total = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
pay = round((total + (total * (tip / 100))) /people, 2)
print(f"Each person should pay: ${pay}")
