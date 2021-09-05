# Task
#
# Perform append, pop, popleft and appendleft methods on an empty deque .
#
# Input Format
#
# The first line contains an integer , the number of operations.
# The next  lines contains the space separated names of methods and their values.
#
# Constraints
#
#
# Output Format
#
# Print the space separated elements of deque .


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n = int(input())

if 0 <= n <= 100:
    # print(n)
    d = deque()
    for i in range(n):
        # print(i)
        ip = input()
        # print(ip)

        if ip.__contains__('appendleft'):
            # print('AL')
            a, b = ip.split()
            d.appendleft(b)
            # print(d)
        elif ip.__contains__('append'):
            # print('A')
            a, b = ip.split()
            d.append(b)
            # print(d)
        elif ip == 'pop':
            # print('p')
            d.pop()
        elif ip == 'popleft':
            # print('pL')
            d.popleft()

    # print(d)
    v = ''
    for i in d:
        v = v + i + ' '
        # print(i)

    print(v)

