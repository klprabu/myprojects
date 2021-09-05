# To find the percentage of a student from dict

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    # print(n)
    # print(student_marks)
    # print(query_name)

    if n >= 2 and n <= 10:
        x = [x for x in student_marks if len(student_marks[x]) == 3]
        # print(x)
        if len(x) > 0:

            for i in x:
                # print(student_marks[i])
                p = student_marks[i]
                s = range(0, 101)

                if any(u in s for u in p):
                    if i == query_name:
                        # print(p)
                        v_tmp = 0
                        for v_add in p:
                            # print(v_add)
                            v_tmp = v_tmp + v_add

                        v_tmp = v_tmp / 3
                        # print(float(v_tmp/3,2))
                        print("%.2f" % v_tmp)






