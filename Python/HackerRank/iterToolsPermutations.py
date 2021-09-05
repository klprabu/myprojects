
# Task
#
# You are given a string .
# Your task is to print all possible permutations of size  of the string in lexicographic sorted order.
#
# Input Format
#
# A single line containing the space separated string  and the integer value .
#
# Constraints
#
#
# The string contains only UPPERCASE characters.
#
# Output Format
#
# Print the permutations of the string S on separate lines.


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations


string , v_len = input().split()
v_len = int(v_len)

#print(string)
#print(v_len)

#print(list(permutations(string,2)))

ls = list(permutations(string,v_len))
ls.sort()
if 0 < v_len <= len(string) and string.isupper():
    for i in ls:
            print(''.join(i))