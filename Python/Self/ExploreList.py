x = [1,2,3,4,5]
for i in range(len(x)):
    print(x[i])

#print(range(len(x)))

a = object()
b = object()
a_list = [a] *10
b_list = [b] *100

print("Type of a_list is ")
print(type(a_list))
print(type(a))
print(len(a_list))
print(hex(id(a_list)))

print("Printing the values of a_list")
#Assinging the values to the list

for j in range(len(a_list)):
    print(j)
    a_list[j] = j
    # print(a_list(j))


for i in range(len(a_list)):
    print("Printing the values of a_list")
    print(a_list[i])


# Reversing the list values

print("Reversing the list values")

alist = [100, 200, 300, 400, 500]
alist.reverse()

for rev in range(len(alist)):
    print(alist[rev])

## Concatenating two list values
print("Concatenating two list values")

res = []
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

for i in range(len(list1)):
    for j in range(len(list2)):
        if i == j:
            print("Value of i is %d, and value of j is %d " % (i,j))
            print(list1[i]+list2[j])
            v = list1[i]+list2[j]
            print(len(res))
            res.append(v)

print(type(res))
print(len(res))

for get in range(len(res)):
    print(res[get])

