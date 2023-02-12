num=int(input("Enter the limit : "))
for i in range(1,num+1):    #defining for loop within limit
    for j in range(1,i+1): #inner loop multiplying each value with 1
        print(i*j," ",end='') #multiplying i and j
    print("\n")