# Kevin Glover
# 2026-7-5
# P4 LAB2
# Use while loop and for loop

'''
Get integer from user
Determine if integer is positive or negative
if number is positive, display multiplication table
if number is negative, tell user program cannot accept it
Ask user to run again?
if yes, run program
if no, end program
'''

run_again = 'yes'

while run_again != "no":
    user_num = int(input("Enter an integer: "))
    if user_num >= 0:
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("Program does not accept negative integers.")

    run_again = input("Do you want to run the program again? ")

print("Program is ending....") 