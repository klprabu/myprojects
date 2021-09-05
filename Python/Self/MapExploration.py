def check(n):
    if n < 0 :
        return 0
    return n


v = [-1.3,4,-5,4,3,22,43,-343]

d = map(check,v)
print(list(d))