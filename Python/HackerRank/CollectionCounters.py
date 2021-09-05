#  RAghu is a shoe shop owner. His shop has  number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.
#
# Your task is to compute how much money  earned.
#
# Input Format
#
# The first line contains , the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains , the number of customers.
# The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.
#
#
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
#
#
# 200


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

shoescnt = int(input())
shoesize = list(input().split())
shoesize = list(map(int, shoesize))
a = [a for a in shoesize if 2 <= a <= 20]
# print(shoesize)
shoecol = Counter(a)
# print(shoecol)
# print(shoecol.keys())
noofcus = int(input())
# print(noofcus)

if 0 < shoescnt < pow(10, 3) and 0 < noofcus <= pow(10, 3):
    Tot_price = 0
    for i in range(noofcus):
        cnt = 0
        ss, price = map(int, input().split())
        if shoecol[ss] > 0 and 20 <= price <= 100:
            # print('Shoe size %s available'%(ss))
            cnt = shoecol[ss]
            shoecol[ss] = cnt - 1
            Tot_price = Tot_price + price

    print(Tot_price)

# if 0 < shoescnt < pow(10,3) and 0 < noofcus <= pow(10,3):

# print(shoecol)

# Tot_price = 0
# for i in range(noofcus):
#     cnt = 0
#     ss, price = map(int,input().split())
#     if shoecol[ss] > 0 :
#     #and 20 < price < 100:
#     #print('Shoe size %s available %d'%(ss,price))
#         print('%d %d'%(ss,price))
#         cnt = shoecol[ss]
#         shoecol[ss] = cnt - 1
#         Tot_price = Tot_price + price

# print(Tot_price)



