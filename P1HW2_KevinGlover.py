# Kevin Glover
# 2026-6-13
# P1HW2
# Basic math program

print("This program calculates and displays travel expenses.")
budget = int(input("Enter budget: "))
destination = input("Enter travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accomodation = int(input("Approximately, how much will you spend on accommodation? "))
food = int(input("How much do you think you will spend on food? "))

print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print("Fuel:", gas)
print("Accommodation:", accomodation)
print("Food:", food)
total_expenses = gas + accomodation + food
print("Total Expenses:", total_expenses)
remaining_budget = budget - total_expenses
print("Remaining Budget:", remaining_budget)