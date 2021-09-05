from collections import deque

d = deque()

str = '1 2 3 4'
a = str.split()
d.append(a)

i = 0
while len(d)!= 0:

    if d[i] >= d[len(d)]:
        cur = d[i]
        nxt = d[i+1]
        lst = d[len(d)]

        if


        d.popleft()
        i = i + 1
    else:
        d.pop()


