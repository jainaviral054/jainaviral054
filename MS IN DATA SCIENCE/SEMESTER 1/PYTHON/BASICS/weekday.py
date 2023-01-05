# Week Day
# easy
# View Solution
# Time Limit: 2 sec
# Memory Limit: 128000 kB
# Problem Statement
# Write a Program to read a number and display the corresponding week day name using if_elif_else.
# Input
# The first line contains the week day number to be printed.
# Output
# Prints the following on given inputs:
# 1- Monday
# 2- Tuesday
# 3- Wednesday
# 4- Thursday
# 5- Friday
# 6- Saturday
# 7- Sunday
# and Invalid on any other input.
# Example
# Sample Input:
# 3

# Sample Output:
# Wednesday
# Generate Expected Outputinfo-icon
# Insert Input


inp = int(input("Enter a number "))

if inp < 8:
    if inp == 1:
        print("Monday")
    elif inp == 2:
        print("Tuesday")
    elif inp == 3:
        print("Wednesday")
    elif inp == 4:
        print("Thursday")
    elif inp == 5:
        print("Friday")
    elif inp == 6:
        print("saturday")
    elif inp == 7:
        print("Sunday")
else:
    print("Invalid input number, please give number between 1 and 7")