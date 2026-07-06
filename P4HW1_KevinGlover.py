# Kevin Glover
# 2026-7-6
# P4HW1
# Grading list
# program Pseudocode


mod_scores = int(input("How many modules are you entering grades for? "))
Grades = []

fix_grade = int

for i in range(mod_scores):
    grade = float(input(f"Enter grade for module {i + 1}: "))
    if grade < 0 or grade > 100:
        print("Invalid grade. Please enter a grade between 0 and 100.")
        fix_grade = float(input(f"Enter a valid grade for module {i + 1}: "))
        Grades.append(fix_grade)
    else:
        Grades.append(grade)

print()
print("------------Results------------")
lowest = min(Grades)
print(f'{"Lowest Grade:"} {lowest:.2f}')
mod_list = Grades.copy()
mod_list.remove(lowest)
print(f'{"Module Grades:"} {mod_list}')
avg = sum(Grades) / len(Grades)
print(f'{"Average Grade:"} {avg:.2f}')
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
else:
    letter_grade = "C"

print(f'{"Letter Grade:"} {letter_grade}')