# List operations
# easy
# View Solution
# Problem Statement
# Execute the del and sort operations on the given list.
# Eg: If input says d 8 then delete the element on the 8th position of the list if the 8th element is not present leave the list as it is.
# If input says a 8 14, then add 14 in 8th place, if 8th place doesn't exist then add the item at the last of the list
# Input
# 1st line: elements on the list
# 2nd line: no of operations ie q
# next q lines: q operations
# Output
# print the list after q operations
# Example
# Input:
# 19 5 15 20 5 8 16 9 12 4 4 4 2 20 9 11
# 2
# a 12 3
# d 3

# Output:
# [2, 3, 4, 4, 4, 5, 5, 8, 9, 9, 11, 12, 16, 19, 20, 20]
# Generate Expected Outputinfo-icon
# Insert Input
# Input
# Output
# Output will be displayed here
# Need Help? Go to Doubt Portal 

list1 = input("Enter list ") # inp  "12 34"
ops = int(input("Enter number of operations"))

list1 = list1.split(" ")
list1 = [int(ele) for ele in list1]

ops_list = []
for op in range(0, ops):
    ops_list.append(input("Enter the operations"))

# list1 = list1.split(" ")

for ops in ops_list:
    ops = ops.split(" ")
    if ops[0] == 'd' and list1[int(ops[1])]:
        del list1[int(ops[1])-1]
    elif ops[0] == "a" and len(list1) > int(ops[1]):
        list1.insert(int(ops[1])-1, int(ops[2]))
    elif ops[0] == 'a':
        list1.append(int(ops[2]))

print(list1)
list1.sort()
print(list1)