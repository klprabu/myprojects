import random

print(random.randint(1, 40))

def createrandom():
    yield random.randint(10000,20000)


for i in createrandom():
    print(i)


# Fib series
print("***************************************")

def fib():
    a,b = 1,1
    while 1==1:
        yield a
        a,b = b,a+b


for i in fib():
    print(i)
    if i > 20:
        break