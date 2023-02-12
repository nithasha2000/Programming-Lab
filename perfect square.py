import math

lists =[]
start=int(input("Enter start : "))
end=int(input("Enter end : "))
for a in range(start,end+1): #defining for loop for each value between the limits
    for b in str(a): #defining for loop for each value in a
        if int(b) % 2 != 0: #checking whether each value in b is even or not
            break
    else:
        root=math.sqrt(a) #finding square of a if each value is even
        if root % 1 == 0:
            lists.append(a)
print("Perfect square : ",lists)