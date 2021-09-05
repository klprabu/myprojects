# This program will get the string and split by k value and substring the string with K
#and check if the substring has duplicate character and removes them and print it

def merge_the_tools(string, k):
    # your code goes here
    ls = len(string)
    cl = 0
    if 0 < ls <= pow(10, 4) and 1 <= k <= ls:
        # print(string)
        cl = int(ls / k)
        lt = [i for i in range(1, len(string) + 1) if i % k == 0]
        # print(lt)

        u = 0
        v = []
        for j in range(len(lt)):
            # print(string[u:lt[j]])
            s = string[u:lt[j]]
            k = ''.join(sorted(set(s), key=s.index))
            print(k)
            # v.append(k)
            u = lt[j]

        # print(v)
        # for i in v:
        #    print(i)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)