# Nobita and Profit
# easy
# View Solution
# Time Limit: 2 sec
# Memory Limit: 128000 kB
# Problem Statement
# Nobita wants to become rich so he came up with some ideas. Nobita buys some gadgets from the future at a price of C and sells them at a price of S to his friends. Now Nobita wants to know how much he gains by selling 1 gadget. As we all know Nobita is weak in maths help him to find the profit he gets
# Input
# You don't have to worry about the input, you just have to complete the function Profit()

# Constraints:-
# 1 <= C <= S <= 1000
# Output
# Print the profit Nobita gets from selling one gadget.
# Example
# Sample Input:-
# 3 5

# Sample Output:-
# 2

# Sample Input:-
# 9 15

# Sample Output:-
# 6
# Generate Expected Outputinfo-icon
# Insert Input
# Input
# Output
# Output will be displayed here
# Need Help? Go to Doubt Portal 

def Profit(c, s):
    profit = s - c
    return profit

C = int(input("Enter the cost price "))
S = int(input("Enter the selling price "))

profit = Profit(C, S)
print(profit)