# Palindrome Number
# easy
# View Solution
# Time Limit: 2 sec
# Memory Limit: 128000 kB
# Problem Statement
# Given a number N, you need to check whether the given number is Palindrome or not. A number is said to be Palindrome when it reads the same from backward as forward.
# Input
# User task:
# Since this is a functional problem you don't have to worry about the input. You just have to complete the function isPalindrome() which contains N as a parameter.

# Constraints:
# 1 <= N <= 9999
# Output
# You need to return "True" is the number is palindrome otherwise "False".
# Example
# Sample Input:
# 5

# Sample Output:
# True

# Sample Input:
# 121

# Sample Output:
# True
# Generate Expected Outputinfo-icon
# Insert Input
# Input
# Output
# Output will be displayed here
# Need Help? Go to Doubt Portal 


def isPalindrome(number):
    number_copy = number
    range_in = len(str(number))
    list1 = []

    for i in range(range_in):
        c = number % 10
        list1.append(c)
        number = number // 10
    print(list1)

    rev = 0

    if len(list1) == 3:
        rev = (list1[0] * 100) + (list1[1] * 10) + (list1[2] * 1)
    if len(list1) == 4:
        rev = (list1[0] * 1000) + (list1[1] * 100) + (list1[2] * 10) + (list1[3] * 1)
    
    print(rev, number_copy)
    if rev == number_copy:
        print("Palindrome Number")
        return True
    else:
        print("Not Palindrome Number")
        return False


result = isPalindrome(number=123)
print(result)

result = isPalindrome(number=1221)
print(result)


num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


def isPalindrome(N):
    string_num = str(N)
    num_list = []
    
    num_list = [i for i in string_num]
    # for i in string_num:
        # num_list.append(i)


    reversed_list = num_list[::-1]
    if num_list == reversed_list:
        return True
    else:
        return False
