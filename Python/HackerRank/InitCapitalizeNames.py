#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    check = 'F'
    v_return = ''

    if 0 < len(s) < 1000:
        for i in range(len(s)):
            if s[i].isalnum() or s[i] == ' ':
                # print(s[i])
                if i == 0:
                    v_name = s[i].upper()
                elif s[i] == ' ':
                    check = 'T'
                    v_name = s[i]
                elif check == 'T' and s[i] != ' ':
                    v_name = s[i].upper()
                    check = 'F'
                else:
                    v_name = s[i]

            v_return = v_return + v_name

            # print(v_return)

    return v_return


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
