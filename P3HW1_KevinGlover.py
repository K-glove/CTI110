# Kevin Glover
# 2026-06-28
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# add grades entered to a list

Grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades
print()
print("------------Results------------")
Lowest = min(Grades)
print(f'{"Lowest Grade:":20s} {Lowest:.2f}')
Highest = max(Grades)
print(f'{"Highest Grade:":20s} {Highest:.2f}')
Sum = sum(Grades)
print(f'{"Sum of Grades:":20s} {Sum:.2f}')
Average = Sum / 6
print(f'{"Average Grade:":20s} {Average:.2f}') 

if Average >= 90:
    print("Your grade is: A")
elif Average >= 80:
    print("Your grade is: B")
elif Average >= 70:
    print("Your grade is: C")
elif Average >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")






