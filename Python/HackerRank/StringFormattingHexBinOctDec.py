#To print the Decimal , octal, binary, hexa values with regular space inbetween


def print_formatted(number):
    # your code goes here
    len_bin = len(bin(number)) - 2
    # print(len_bin)
    space_padding = ' ' * (len_bin)
    v = ''
    if 1 <= number <= 99:
        for i in range(1, number + 1):
            oc = oct(i)
            hx = hex(i)
            hxx = str(hx[2:]).upper()
            bi = bin(i)
            bii = str(bi[2:])
            # print(str(i)+space_padding+str(oc[2:])+space_padding+str(hx[2:]).upper()+bii.rjust(len_bin,' '))
            print(str(i).rjust(len_bin, ' ') + str(oc[2:]).rjust(len_bin + 1, ' ') + hxx.rjust(len_bin + 1,
                                                                                               ' ') + bii.rjust(
                len_bin + 1, ' '))

            # print('%s%s%s'%(str(i)+len_bin+str(oc[2:])+len_bin))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)