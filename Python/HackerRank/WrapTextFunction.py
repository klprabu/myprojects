#Textwrap -- To wrap a sentence with the value given

import textwrap


def wrap(string, max_width):
    if 0 < len(string) < 1000 and 0 < max_width < len(string):
        Textobject = textwrap.TextWrapper(max_width)
        TextList = Textobject.wrap(string)
        v = ''

        for i in range(len(TextList)):
            # print(i)
            if i == len(TextList) - 1:
                v = v + TextList[i]
            else:
                v = v + TextList[i] + '\n'

        # print(v)
        return v


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)