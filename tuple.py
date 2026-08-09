#Tuple-->immutable, contain duplicate,ordered and hetrogenous
tuple2=(1,5,5,2.5,"hello",True,[1,2,3,4])
print (tuple2)

#two main method-->index() ,count()
print(tuple2.count(5))  #2
print(tuple2.index(5))   #1

tuple1=1,2,3,"hello",False,[1,6,7,8]
print(tuple1)
print(type(tuple1))


#for single element
tup=(10)
print(tup)
print(type(tup)) #<class 'int'>

tup1=(10,)
print(tup1)
print(type(tup1)) #<class 'tuple'>

#traversing
for i in tuple2:
    print(i)

print(tuple2[-1]) #[1, 2, 3, 4]
print(tuple2[-2]) #True

#tuple Slicing
print(tuple2[1:5])  #(5, 5, 2.5, 'hello')

#Step in Slicing
print(tuple2[0:7:2]) #(1, 5, 'hello', [1, 2, 3, 4])

#reverse a tuple
print(tuple2[::-1]) #([1, 2, 3, 4], True, 'hello', 2.5, 5, 5, 1)

numbers = (40, 10, 30, 20)
print(sum(numbers)) #100
print(len(numbers)) #4
print(max(numbers)) #40
print(min(numbers)) #10

#Checking Whether an Element Exists
print(20 in numbers)  #True
print(50 in numbers)  #False

result = sorted(numbers)

print(result) #[10, 20, 30, 40]
print(type(result)) #<class 'list'>

#Converts another iterable into a tuple.
numbers1 = [10, 20, 30]
result1 = tuple(numbers1)
print(result1)  #(10, 20, 30)

#You can convert a string too
text = "ABC"
print(tuple(text))  #('A', 'B', 'C')


#Tuple Concatenation
a=(1,2,3,4,5)
b=(6,7,8,9,10)
c=a+b
print(c)         #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(c))    #<class 'tuple'>


#Tuple Repetition
d=(1,2,3)
print(d * 3)   #(1, 2, 3, 1, 2, 3, 1, 2, 3)


#Tuple Unpacking
student = ("Priyanshu", 23, "CSE-DS")

name, age, branch = student

print(name)  #Priyanshu
print(age)  #23
print(branch)   #CSE-DS
print(student[0])#Priyanshu


#'*' in Tuple Unpacking
numbers = (10, 20, 30, 40, 50)

a, *b = numbers

print(a)        #10
print(type(a))  #<class 'int'>
print(b)          #[20, 30, 40, 50]
print(type(b))   #<class 'list'>