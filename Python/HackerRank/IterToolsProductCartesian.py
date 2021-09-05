# You are given a two lists  and . Your task is to compute their cartesian product X.
#
# A = [1, 2]
# B = [3, 4]
#
# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
# Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order.


# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

a = list(input().split())
b = list(input().split())

a = list(map(int, a))
b = list(map(int, b))

# print(a)
# print(b)

if all(i >= 0 and i < 30 for i in a) and all(i >= 0 and i < 30 for i in b):
    if len(a) == len(set(a)) and len(b) == len(set(b)):
        v = ''
        # print(list(product((1,2),(3,4))))
        for i in list(product(a, b)):
            # print(i)
            v = v + str(i) + ' '

        print(v)
