# Positive or Negative
# easy
# View Solution
# Time Limit: 2 sec
# Memory Limit: 128000 kB
# Problem Statement
# Write a program to print a number is positive/negative using if- else.
# Input
# The first line contains the number to be checked.

# Constraints:
# -100000<=n<=100000
# Output
# Prints "Positive number" if the number is positive, "Zero" if the number is zero and "Negative number" if the number is negative.
# Example
# Sample input:
# 33

# Sample Output:
# Positive number
# Generate Expected Outputinfo-icon
# Insert Input
# Input
# Output
# Output will be displayed here
# Need Help? Go to Doubt Portal

inp = int(input("Enter a number "))

if inp > 0:
    print("positive number")
elif inp < 0:
    print("Negative number")
else:
    print("Zero")