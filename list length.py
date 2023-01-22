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
    val2=int(input()) #inputting list1 items
    list2.append(val2)
print("List1 :",list1)
print("List2 :",list2)
if(n1==n2): #check whether n1 equal to n2
    print("List1 and List2 are of same length") #printing the result
else:
    print("list1 and List2 are not same length")