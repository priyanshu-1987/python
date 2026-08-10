#Set = unordered + unique + mutable
a={10,20,30,40,10,10,30,50}
print(a)

#traversing
for i in a:
    print(i)

#Set Does NOT Support Indexing
#print(a[0]) #generate error


#Empty Set
a1 = {}
print(type(a1))  #<class 'dict'>

a2 = set()
print(type(a2))  #<class 'set'>

""" Note:
    {} → empty dictionary
    set() → empty set  """

#tupel-->set
b=(1,2,3,4,5,3,1,2)
c=set(b)
print(c)    #{1, 2, 3, 4, 5}
print(type(c))  #<class 'set'>

#List -->set
b1=[1,2,3,4,2,1,5]
c1=set(b1)
print(c1)    #{1, 2, 3, 4, 5}
print(type(c1))  #<class 'set'>

#String-->set
str="Priyanshu"
c2=set(str)
print(c2)   #{'a', 'h', 'y', 's', 'P', 'u', 'i', 'r', 'n'}
print(type(c2))  #<class 'set'>


#add element
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)   #{40, 10, 20, 30}
numbers.update([ 50, 60,70])
print(numbers)    #{70, 40, 10, 50, 20, 60, 30}
numbers.remove(70)
print(numbers)  #{40, 10, 50, 20, 60, 30}
#numbers.remove(90) # generate error
numbers.discard(10)
print(numbers)    #{40, 50, 20, 60, 30}
numbers.discard(90) #not generate error
x=numbers.pop()
print(x)             #40
print(numbers)       #{50, 20, 60, 30}
numbers.clear()      #set still exists, but it is empty
print(numbers)       #set()
numbers1={1,2,3,4,5,6}
del numbers1         #gives a NameError because the variable no longer exists.
# print(numbers1)  generate NameError 