#Following is the exercise, function provided:
from functools import partial
def func(u,v,w,x):
    print('u - %d' % u)
    print('v - %d' % v)
    print('w - %d' % w)
    print('x - %d' % x)
    print('u - %d v - %d' %(u,v))
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function

dbl = partial(func,5,5,10)
print(dbl(5))