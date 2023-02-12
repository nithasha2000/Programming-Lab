n=int(input("Enter a number : "))
print("The factors of ",n," : ")
for i in range(1,n+1): #defining for loop from 1 to n
    if(n%i==0): #checking whether each number is a factor of n
        print(i)