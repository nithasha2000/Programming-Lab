n=int(input("Enter a number : "))
a,b=0,1 #initializing a,b with 0 and 1
sum=0
print("Fibonacci series of",n,"terms : ")
print(a)
print(b)
for i in range(2,n):
    sum=a+b #adding numbers
    a=b #swapping variables
    b=sum
    print(sum)
    i=i+1
