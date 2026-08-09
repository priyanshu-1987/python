#list --> mutable,containt duplicates, ordered and hetrogenous
list=[1,2,3,3,3,2.5,"hello",True]
list[2]=75
print(list[0:8])

#traversing
for i in list:
    print(i)

#inbuild method
num=[]
num.append(6)
num.append(35)
num.append(67)
num.append(67)

num.insert(1,35)
print (num)             #[6, 35, 35, 67, 67]
num.extend([1,2,3,4])
print (num)              #[6, 35, 35, 67, 67, 1, 2, 3, 4]
num.remove(35)
print(num)               #[6, 35, 67, 67, 1, 2, 3, 4]
print(num.count(67))     #2
num.sort()
print (num)              #[1, 2, 3, 4, 6, 35, 67, 67]
num.reverse()
print(num)                #[67, 67, 35, 6, 4, 3, 2, 1]

new=num.copy()
num.clear()
print(num)                #[]
print(new)                #[67, 67, 35, 6, 4, 3, 2, 1]


