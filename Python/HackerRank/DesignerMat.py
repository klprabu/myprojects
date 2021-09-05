# Set the design as per the input
#Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

#Mat size must be X. ( is an odd natural number, and  is  times .)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.

# Enter your code here. Read input from STDIN. Print output to STDOUT

rows, cols = input().split()

# print(rows)
# print(cols)

rows = int(rows)
cols = int(cols)

hyp = '-'
pip = '.|.'
print_hyp = 0
odd_nos = []
v_odd_nos = []

if rows % 2 != 0 and cols % 3 == 0 and 5 < rows < 101 and 15 < cols < 303:

    for j in range(cols):
        if j % 2 != 0:
            odd_nos.append(j)
            if j * 3 >= cols:
                break

    # print(odd_nos)
    r_odd_nos = odd_nos[:len(odd_nos) - 1].copy()
    r_odd_nos.reverse()
    v_odd_nos = odd_nos + r_odd_nos

    # print(v_odd_nos)

    itr = 0
    check = 0

    for i in range(1, rows + 1):
        # v = i * 3
        itr = i - 1
        # print(itr)
        n = v_odd_nos[itr] * 3
        print_hyp = int((cols - n) / 2)
        check = int(len(v_odd_nos) / 2) + 1
        # print(v_odd_nos[check])
        if i < check:
            print(hyp * print_hyp + pip * v_odd_nos[itr] + hyp * print_hyp)
        elif i == check:
            print(hyp * int((cols - 7) / 2) + 'WELCOME' + hyp * int((cols - 7) / 2))
        elif i > check:
            print(hyp * abs(print_hyp) + pip * v_odd_nos[itr] + hyp * abs(print_hyp))