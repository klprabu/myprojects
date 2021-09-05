# This program will design the alphabet and draw a rangoli

def print_rangoli(size):
    # your code goes here
    if 0 < size < 27:
        # print(size)
        rows = size + (size - 1)
        cols = rows + (rows - 1)

        # print('No. of rows %d and no. of cols %d'%(rows,cols))

        hyp = '-'
        letter = ''

        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

        rn = []

        for i in range(size):
            rn.append(alpha[i])

        rn.reverse()
        # print(rn)

        rrn = rn.copy()
        rrn.reverse()
        rrn = rrn[1:]

        # print(rrn)

        # print(rn+rrn)
        vn = rn + rrn

        # for i in range(1,cols+1):
        for j in range(len(vn)):
            # print(j)
            if j == 0:
                loh = int((cols - 1) / 2)
                print(hyp * loh + vn[j] + hyp * loh)

            elif rows - size >= j:
                a = len(vn) - j
                # print(vn[:j]+vn[a-1:])
                l1 = vn[:j] + vn[a - 1:]
                ll1 = [ll1 + '-' for ll1 in l1]

                listToStr = ''.join([str(elem) for elem in ll1])
                # print(listToStr)
                # print(listToStr[:len(listToStr)-1])
                listToStr = listToStr[:len(listToStr) - 1]
                # print(listToStr)
                # p = int(cols - len(listToStr))

                print(listToStr.center(cols, '-'))

            elif rows - size < j:
                a = rows - j
                # print(vn[:a]+vn[j+1:])
                lf = vn[:a] + vn[j + 1:]
                lf1 = [lf1 + '-' for lf1 in lf]

                listToStr1 = ''.join([str(elem) for elem in lf1])
                # print(listToStr1)
                # print(listToStr1[:len(listToStr1)-1])
                listToStr1 = listToStr1[:len(listToStr1) - 1]
                # print(listToStr1)
                print(listToStr1.center(cols, '-'))

        # if j+size == rows:
        #     break


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)