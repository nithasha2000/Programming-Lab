list1=[]
list2=[]
sum1=0
sum2=0
n1=int(input("Enter the limit of 1st list : "))
print("Enter the values of 1st list : ")
for i in range(0,n1):
    val1=int(input()) #inputting list1 items
    list1.append(val1)
n2=int(input("Enter the limit of 2nd list : "))
print("Enter the values of 2nd list : ")
for i in range(0,n2):
    val2=int(input()) #inputting list2 items
    list2.append(val2)
print("List1 :",list1)
print("List2 :",list2)
check=set(list1) and set(list2) #set AND operation to find any common elements
if check:
    print("Common elements found")
else:
    print("No common elements found")

