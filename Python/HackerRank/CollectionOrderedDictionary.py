# This program is a introduction to the ordered dict. It is useful because the dictionary values
# are stored as the order which was inserted. Whereas the normal dictornary order is always jumbled

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
import re

n = int(input())

if 0 <= n <= 100:
    ordic = OrderedDict()
    for i in range(0, n):
        pr = 0
        v = input()
        # print(v)
        # print(" ".join(re.findall("[a-zA-Z]+", v)))
        okey = " ".join(re.findall("[a-zA-Z]+", v))
        oval = int(''.join(re.findall(r'\d+', v)))

        if okey in ordic:
            # print('Already Exists')
            pr = ordic[okey]
            pr = pr + oval
            ordic[okey] = pr
        else:
            ordic[okey] = oval

    # print(ordic.keys())
    for p in ordic:
        # print(p)
        # print(ordic[p])
        print('%s %d' % (p, ordic[p]))
    # print('%s %d'%(ordic.keys(),ordic.values()))
