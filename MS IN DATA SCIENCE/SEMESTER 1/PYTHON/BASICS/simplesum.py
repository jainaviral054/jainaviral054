# Simple Sum
# easy
# View Solution
# Time Limit: 2 sec
# Memory Limit: 128000 kB
# Problem Statement
# Given three integers A, B, and C, your task is to print the sum of these three integers.
# Input
# The input contains 3 integers separated by spaces A, B, and C.

# Constraints:-
# 1 <= A, B, C <= 100
# Output
# Print the sum of A, B and C.
# Example
# Sample Input
# 1 2 3

# Sample Output:-
# 6

# Sample Input:-
# 5 4 2

# Sample Output:-
# 11
# Generate Expected Outputinfo-icon
# Insert Input
# Input
# Output
# Output will be displayed here
# Need Help? Go to Doubt Portal 


inp = input("Enter 3 integers ") # inp  "12 34 67"
inp = inp.split(" ")
print(inp)

A, B, C = int(inp[0]), int(inp[1]), int(inp[2])

sum = A + B + C
print(sum)