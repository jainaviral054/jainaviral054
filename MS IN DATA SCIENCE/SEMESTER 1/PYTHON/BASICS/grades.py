# Ram Grades
# easy
# View Solution
# Time Limit: 2 sec
# Memory Limit: 128000 kB
# Problem Statement
# Ram is studying in Class V and has four subjects, each subject carry 100 marks. He passed with flying colors in his exam, but when his neighbour asked how much percentage did he got in exam, he got stuck in calculation. Ram is a good student but he forgot how to calculate percentage. Help Ram to get him out of this problem.
# Input
# First line contains four variables a, b, c and d.

# Constraints
# 1<= a, b, c, d <= 100
# Output
# Print single line containing the percentage.
# Example
# Sample Input 1:
# 25 25 25 25

# Sample Output 1:
# 25

# Sample Input 2:
# 75 25 75 25

# Sample Output 2:
# 50
# Generate Expected Outputinfo-icon
# Insert Input
# Input
# Output
# Output will be displayed here
# Need Help? Go to Doubt Portal 

inp = input("Enter a, b, c and d integers ") # inp  "12 34"
inp = inp.split(" ")
print(inp)

a, b, c, d = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])
percent = ((a + b + c + d) / 400) * 100
print(percent)