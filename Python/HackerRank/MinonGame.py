import re
import itertools


def minion_game(string):
    # your code goes here

    cons = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    vows = ['A', 'E', 'I', 'O', 'U']

    if re.match(r'(?:[A-Z]+|[a-z]+)$', string) and 0 < len(string) < pow(10, 6):
        # print(string)
        x = set(x for x in string if x in cons)
        # print(x)

        stuart = {}

        for y in x:
            # print('value of y is %s'%y)
            k = string[string.find(y):]

            # print(k)

            w = ''
            for j in range(len(k)):
                w = w + k[j]
                # print(w)

                res = 0
                for i in range(len(k)):
                    if k[i:i + len(w)] == w:
                        res += 1

                # print(res)
                stuart[w] = res

        s_point = sum(stuart.values())

        # print(s_point)

        #####################################################################

        x = set(x for x in string if x in vows)
        # print(x)

        kevin = {}

        for y in x:
            # print('value of y is %s'%y)
            k = string[string.find(y):]

            # print(k)

            w = ''
            for j in range(len(k)):
                w = w + k[j]
                # print(w)

                res = 0
                for i in range(len(k)):
                    if k[i:i + len(w)] == w:
                        res += 1

                # print(res)
                kevin[w] = res

        # print(kevin)
        k_point = sum(kevin.values())

        # print(k_point)

        if s_point > k_point:
            print('%s %d' % ('Stuart', s_point))
        else:
            print('%s %d' % ('Kevin', k_point))


if __name__ == '__main__':
    s = input()
    minion_game(s)

##############################
#### improved code


import re
import itertools


def minion_game(string):
    vowel = ['A', 'E', 'I', 'O', 'U']
    S = 0
    K = 0
    for i in range(len(string)):
        if string[i] in vowel:
            K += len(string) - i
        else:
            S += len(string) - i
            # print('%d  %d'%(S,i))
    if S > K:
        print("Stuart" + " " + "%d" % S)
    elif K > S:
        print("Kevin" + " " + '%d' % K)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)




