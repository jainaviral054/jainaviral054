# 5 stars
# easy
# View Solution
# Time Limit: 2 sec
# Memory Limit: 128000 kB
# Problem Statement
# In this task you have to print 5 stars ('*') vertically and 5 horizontally.
# You are given functions to complete. Don't worry about the ins and outs of functions just print 5 vertical stars in vertical5 and 5 horizontal stars in horizontal5
# Input
# User Task:
# Your task is to complete the functions vertical5() and horizontal5() given below to print the stars.
# Output
# Print 5 vertical stars in vertical5 and 5 horizontal stars(separated by a whitespace) in horizontal5 function.
# Example
# Sample Output:-
# *
# *
# *
# *
# *

# * * * * *

# Explanation:- 5 vertical and horizontal stars will be printed

# Note:- You don't need to print the extra blank line it will be printed by the driver code
# Generate Expected Outputinfo-icon
# Insert Input
# Input
# Output
# Output will be displayed here
# Need Help? Go to Doubt Portal


def vertical5():
    for i in range(5):
        print("*")


def horizontal5():
    for i in range(5):
        print("*", end = " ")

def pattern():
    for i in range(6):
        # print("*")
        for j in range(1):
            print("*"*i)

vertical5()
horizontal5()

pattern()