# For Loop
# easy
# View Solution
# Time Limit: 2 sec
# Memory Limit: 128000 kB
# Problem Statement
# Given an integer n, For each i (1<=i<=n) if i is even print "even" else print "odd".
# Input
# User task:
# Since this will be a functional problem, you don't have to take input. You just have to complete the functions For_Loop() that takes the integer n as parameter.

# Constraints:
# 1 <= n <= 100
# Output
# Print even or odd for each i (1<=i<=n) separated by white spaces.
# Example
# Sample Input:
# 5

# Sample Output:
# odd even odd even odd

# Sample Input:
# 2

# Sample Output:
# odd even
# Generate Expected Outputinfo-icon
# Insert Input
# Input
# Output
# Output will be displayed here
# Need Help? Go to Doubt Portal 


range_in = int(input("Enter the range for even and odd"))
range_in = range_in + 1

out_str = ""

for i in range(1, range_in):
    # print(i)
    if i % 2 == 0:
        out_str = out_str+ "Even" + " " 
        # print("Even", end=" ")
    else:
        out_str = out_str + "Odd" + " " 
        # print("Odd", end=" ")
    
print(out_str)