list=[]
n=int(input("Enter the limit : ")) #inputting limit
print("Enter the list of integers :")
for i in range(0,n):
    val=int(input()) #inputting list items
    if(val>100): #condition to check whether numbers are greater than 100
        list.append("over")
    else:
        list.append(val)

print("New List :",list)