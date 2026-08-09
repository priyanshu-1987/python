a=12
b=2

#Arithmetic operators
c=a+b #addition
d=a-b #subtraction
e=a*b   #multiplication
f=a/b  #division
g=a//b  #floor division
h=a%b   #modulus
i=a**b   #exponentiation
print(c,d,e,f,g,h,i) #14 10 24 6.0 6 0 144

#Compound assignment operator
a+=b  # equivalent to a = a + b
print(a) #14
a-=b  # equivalent to a = a - b
print(a) #12
a*=b  # equivalent to a = a * b
print(a) #24
a/=b  # equivalent to a = a / b
print(a) #12.0
a//=b  # equivalent to a = a // b
print(a) #6.0
a**=b  # equivalent to a = a ** b
print(a) #36.0
a%=b  # equivalent to a = a % b
print(a) #0.0

a=12
b=2

#Comparison operators
print(a==b) #False
print(a!=b) #True
print(a>b) #True
print(a<b) #False
print(a>=b) #True
print(a<=b) #False

#Logical operators
print(a and b) #2
print(a or b) #12
print(not a) #False