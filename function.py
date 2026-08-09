def fun():
    print("hello")

fun()

#Functions parameters and arguments

def hello(name):  #name is parameter
    print(f"hello ,my name is {name}")

hello("Priyanshu")  # "priyanshu" is argument


#types of argument--> positional argument, default argument, keyword argument
#positional argument
def add(a,b):
    print(a+b)

add(3,8)

# default argument
def add1(a,b=45):  #b=45 is a default argument
    print(a+b)

add1(12)
add1(12,18)

#keyword argument
def intro(name , age):
    print(f"my name is {name} and my age is {age}")

intro(age=23,name="Priyanshu")