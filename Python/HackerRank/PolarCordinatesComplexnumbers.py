# Task
# You are given a complex . Your task is to convert it to polar coordinates.
#
# Input Format
#
# A single line containing the complex number . Note: complex() function can be used in python to convert the input as a complex number.
#
# Constraints
#
# Given number is a valid complex number
#
# Output Format
#
# Output two lines:
# The first line should contain the value of .
# The second line should contain the value of .



import cmath
# Enter your code here. Read input from STDIN. Print output to STDOUT

a = complex(input())
print(round(abs(a),3))
print(round(cmath.phase(a),3))


