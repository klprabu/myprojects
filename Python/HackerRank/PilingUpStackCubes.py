# Enter your code here. Read input from STDIN. Print output to STDOUT\\

from collections import deque

for _ in range(int(input())):
    _, queue = input(), deque(map(int, input().split()))

    for cube in reversed(sorted(queue)):
        # print('Cube is %d'%cube)
        # print('queue[-1] is %d'%queue[-1])
        # print('queue[0] is %d'%queue[0])
        if queue[-1] == cube:
            queue.pop()
        # print(queue[-1])
        elif queue[0] == cube:
            queue.popleft()
        # print(queue[0])
        else:
            print('No')
            break
    else:
        print('Yes')
