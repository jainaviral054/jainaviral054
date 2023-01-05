# Waiting Time
# easy
# View Solution
# Time Limit: 2 sec
# Memory Limit: 128000 kB
# Problem Statement
# Sara is standing in a line for her turn to see the doctor. There are N people standing in front of Sara and for each person, the doctor takes exactly X minutes. Sara wants to know the time after which her number comes. Since Sara is weak in maths, your task is to calculate the time for her.
# Input
# You don't have to worry about the input, you just have to complete the function waitingTime()

# Constraints:-
# 1 <= N <= 1000
# 1 <= X <= 1000
# Output
# Return the total time Sara needs to wait before her turn in minutes.
# Example
# Sample Input:-
# 5 3

# Sample Output:-
# 15

# Sample Input:-
# 3 2

# Sample Output:-
# 6
# Generate Expected Outputinfo-icon
# Insert Input
# Input
# Output
# Output will be displayed here
# Need Help? Go to Doubt Portal 

def waitingTime(n, x):
    return n * x

inp = input("Enter D and Q integers ") # inp  "12 34"
inp = inp.split(" ")
print(inp)

N, X = int(inp[0]), int(inp[1])
wait_mi = waitingTime(N, X)
print(wait_mi)