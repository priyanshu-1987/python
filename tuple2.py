#Nested Tuple
data=(
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
print(data)  #((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(data[0])  #(1, 2, 3)
print(data[1][2])  #6


#Tuple Containing a List
data1 = (10, 20, [30, 40])
data1[2].append(50)
print(data1)   #(10, 20, [30, 40, 50])
print(type(data1))  #<class 'tuple'>


#Comparing Tuples
a = (1, 2, 3)
b = (1, 2, 3)
print(a == b)  #True
print((1,2)<(2,1))  #True  (Python compares elements from left to right.)


#Tuple as Dictionary Key
location = {
    (28.61, 77.20): "Delhi",
    (19.07, 72.87): "Mumbai"
}

print(location[(28.61, 77.20)])   #Delhi