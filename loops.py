#For loops
#range(start, stop, step)

############## range for numbers ############
for i in range(2,11,2): 
    print(i) #2 4 6 8 10

for i in range(6,0,-1):
    print(i) #6 5 4 3 2 1


############### range for strings #############
st="hello"
for i in range(len(st)):
    print(st[i]) #h e l l o

for i in st:
    print(i) #h e l l o


################# Break continue else ##############
for i in range(1,8):
    if i==5:
        break
    print(i) #1 2 3 4

for i in range(1,8):
    if i==5:
        continue
    print(i) #1 2 3 4 6 7

for i in range(1,8):
    if i==5:
        continue
    print(i) #1 2 3 4 6 7
else:
    print("loop completed") #loop completed  

for i in range(1,8):
    if i==5:
        break  # terminate of loop
    print(i) #1 2 3 4
else:
    print("loop completed") #not printed because loop is not completed

############# while loops ###############
i=1
while i<8:
    if i==5:
        break
    print(i) #1 2 3 4
    i+=1
else:
    print("loop completed") #not printed because loop is not completed
