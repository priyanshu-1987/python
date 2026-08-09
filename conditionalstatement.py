
age=int(input("Enter your age: "))
if(age>0):
    print("positive")

if(age%2==0):
    print("even")
else:
    print("odd")

if(age<18):
    print("minor")
elif(age>=18 and age<60):
    print("adult")
else:
    print("senior citizen")