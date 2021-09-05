numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
#print(numbers)
#print(len(numbers))

#newlist = [[] for i in range(len(numbers)) if numbers[i] > 0]

newlist = [int(i) for i in numbers if i > 0]
print(newlist)