# Kevin Glover
# 2026-07-06
# P4HW2
# This program will calculate and display an employees weekly pay

name = input("Enter employee's name or 'done' to finish: ")

overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != "done":
    employee_count += 1
    hours = float(input("How many hours did " +name+ " work this week? "))
    payrate = float(input("What is " +name+ "'s hourly pay rate? "))
    


    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * payrate * 1.5
        regular_pay = 40 * payrate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * payrate
        gross_pay = regular_pay
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay


    print("------------------------------------------")
    print("Emplyee Name: ", name)
    print()
    print(f'{"Hours Worked":<16} {"Pay Rate":<12} {"Overtime Pay":<15} {"Regular Pay":<14} {"Gross Pay":<12}')
    print("---------------------------------------------------------------------------------------")
    print(f"{hours:<16}{payrate:<13.2f}{overtime_pay:<17.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}")


    name = input("Enter employee's name or 'done' to finish: ")

print("Total number of employess entered: ", employee_count)
print("Total overtime pay for all employees: $", format(overtimepay_total,',.2f'))
print("Total regular pay for all employees: $", format(regularpay_total,',.2f'))
print("Total gross pay for all employees: $", format(grosspay_total,',.2f'))