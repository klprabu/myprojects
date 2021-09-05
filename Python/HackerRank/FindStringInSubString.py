a = 'abcdcdc'
print(a)

b = a.__contains__('cdc')
print(b)


b = a.count('cdc',4,len(a))
print(b)

b = [1,2,3]
print(b.clear())