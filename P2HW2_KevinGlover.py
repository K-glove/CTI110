# Kevin Glover
# 2026-6-20
# P2HW2
# Grading list
# program Pseudocode

Module1 = float(input("Enter grade for module 1: "))
Module2 = float(input("Enter grade for module 2: "))
Module3 = float(input("Enter grade for module 3: "))
Module4 = float(input("Enter grade for module 4: "))
Module5 = float(input("Enter grade for module 5: "))
Module6 = float(input("Enter grade for module 6: "))
Grades = [Module1, Module2, Module3, Module4, Module5, Module6]
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