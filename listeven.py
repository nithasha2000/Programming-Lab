n=int(input("Enter the limit : "))
list=[]
print("Enter the values : ")
for i in range(0,n):
    val=int(input()) #inputting items to the list
    if val % 2 != 0: #checking each value is odd or even
        list.append(val) #if odd, append value to the list
print(" New List : ",list)