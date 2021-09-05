if __name__ == '__main__':
    N = int(raw_input())

    v = []

    for _ in range(N):
        s = str(raw_input())
        a = s.split(" ")
        v.append([x for x in a])
        # print(v)

        # for i in a:
        # print(i)
    arr = []

    for j in v:
        # print(j[0])
        if j[0] == "append":
            arr.append(int(j[1]))
        elif j[0] == "print":
            print(arr)
        elif j[0] == "insert":
            arr.insert(int(j[1]), int(j[2]))
        elif j[0] == "pop":
            arr.pop()
        elif j[0] == "remove":
            arr.remove(int(j[1]))
        elif j[0] == "sort":
            arr.sort()
        elif j[0] == "reverse":
            arr.reverse()

    # print(arr)
