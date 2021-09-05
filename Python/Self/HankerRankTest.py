if __name__ == '__main__':
    v_name = []
    v_score = []

    for cnt in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())

        v_name.append(name)
        v_score.append(score)

    # print(cnt+1)
    n = cnt + 1

    # print(v_score)
    uni = []
    uv = 0

    for unique in v_score:
        if unique not in uni:
            uv = uv + 1
            uni.append(unique)

    # print(uni)
    # print(uv)

    if uv > 1 and n >= 2 and n <= 5:

        # print(v_name)
        # print(v_score)

        student = []
        student_list = []

        for i in range(len(v_name)):
            student = [v_name[i], v_score[i]]
            student_list.append(student)

        student_list.sort(key=lambda x: x[1])
        # print(student_list)

        prev = 99
        for k in student_list:
            if prev < k[1]:
                # print(k[1])
                v = k[1]
                # v.append(k[1])
                break
            prev = k[1]

        res = []

        for s in student_list:
            if s[1] == v:
                res.append(s[0])
                res.sort()

        for get in res:
            print(get)
