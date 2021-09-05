#You are given  words. Some words may repeat.
# For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.
# See the sample input/output for clarification

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())

if 1 <= n <= pow(10, 5):
    ordic = OrderedDict()
    for i in range(n):
        v = input()

        if v in ordic:
            # prev = ordic[v]
            cnt = int(ordic[v]) + 1
            ordic[v] = cnt
        else:
            ordic[v] = 1

    # print(ordic)
    print(len(ordic))
    pt = ''
    for k in ordic.values():
        pt = pt + str(k) + ' '
        # print(str(k))

    print(pt)
    # print(''.join([int(x) for x in ordic.values()]))