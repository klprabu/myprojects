# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from math import acos, degrees

ab = int(input())
bc = int(input())

if 0 < ab <= 100 and 0 < bc <= 100:
    ca = math.sqrt(pow(ab, 2) + pow(bc, 2))
    # print(ca)
    teta = degrees(acos((ab * ab + bc * bc - ca * ca) / (2.0 * ab * bc)))
    an = teta / 2
    if round(float(str(an - int(an))[1:]), 2) >= 0.5:
        an = math.ceil(an)
    else:
        an = math.floor(an)

if 0 < an < 90:
    print(str(an) + u'\N{DEGREE SIGN}')


# Below program can run for all test cases


#import math
AB,BC=int(input()),int(input())
hype=math.hypot(AB,BC)                      #to calculate hypotenuse
res=round(math.degrees(math.acos(BC/hype))) #to calculate required angle
degree=chr(176)                                #for DEGREE symbol
print(res,degree, sep='')