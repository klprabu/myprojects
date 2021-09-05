# This program will swap the casee for each letter in a sentence

def swap_case(s):
    v_str = ''
    if len(s) >= 0 and len(s) <= 1000:
        for v in range(len(s)):
            # print(s[v])
            tmp = s[v]
            if tmp.isupper():
                # print('upper')
                v_tmp_str = tmp.lower()
            else:
                # print('lower')
                v_tmp_str = tmp.upper()

            v_str = v_str + v_tmp_str

    # print(v_str)
    return v_str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)