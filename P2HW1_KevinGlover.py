# Kevin Glover
# 2026-6-20
# P2HW1
# Edit/enhancement of P1HW2

print("This program calculates and displays travel expenses.")
budget = float(input("Enter budget: "))
destination = input("Enter travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accomodation = float(input("Approximately, how much will you spend on accommodation? "))
food = float(input("How much do you think you will spend on food? "))

print("------------Travel Expenses------------")
print(f'{"Location:":20s} {destination:10s}')
print(f'{"Initial Budget:":20s} ${budget:.2f}')
print(f'{"Fuel:":20s} ${gas:.2f}')
print(f'{"Accommodation:":20s} ${accomodation:.2f}')
print(f'{"Food:":20s} ${food:.2f}')
total_expenses = gas + accomodation + food
print(f'{"Total Expenses:":20s} ${total_expenses:.2f}')
print("--------------------------------------")
print()
remaining_budget = budget - total_expenses
print(f'{"Remaining Budget:":20s} ${remaining_budget:.2f}')