# Kevin Glover
# 2026-06-28
# P3HW2
# This program will calculate and display an employees weekly pay

Name = input("Enter employee's name: ")
Hours = float(input("Enter number of hours worked this week: "))
PayRate = float(input("Enter employee's hourly pay rate: "))
Overtime = input("Has the employee worked overtime? (Y/N): ")
if Overtime == "Y" or Overtime == "y":
    OvertimeHours = float(input("Enter number of overtime hours worked: "))
    OvertimePayRate = PayRate * 1.5
    OvertimePay = OvertimeHours * OvertimePayRate
if Overtime == "N" or Overtime == "n":
    OvertimePay = 0
print("------------------------------------------")
print(f"Employee Name: {Name}")
print()
print(f"Hours Worked    Pay Rate    Overtime Hours    Overtime Pay    Regular Pay    Gross Pay")
print("---------------------------------------------------------------------------------------")
print(f"{Hours:<16}{PayRate:<13.2f}{OvertimeHours if Overtime == 'Y' or Overtime == 'y' else 0:<18}{OvertimePay:<17.2f}{Hours * PayRate:<15.2f}{Hours * PayRate + OvertimePay:<.2f}")



