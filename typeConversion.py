#convert into their UNICODE values
a="A"
print(ord(a)) #65
b=72
print(chr(b)) #H
c="Priyanshu"
print(ord(c[2])) #105
print(c[-1], c[2]) #u i
#c[start:end:step]  #start is inclusive, end is exclusive, step is optional
print(c[0:7:2]) #Pias
z="😅"
print(ord(z)) #128517
y="🤧"
print(ord(y)) #129319
x="🐼"
print(ord(x)) #128060


#Type Conversion
d=12
d=str(d) #int to string
print(type(d)) #string
print(d) #12
e=27
e=float(e) #int to float
print(type(e)) #float
print(e) #27.0
f=12
g="hello"
h=0
print(bool(f)) #True
print(bool(g)) #True    
print(bool(h)) #False

#7 falsy values in python
#False, 0, 0.0, "", [], {}, set()

