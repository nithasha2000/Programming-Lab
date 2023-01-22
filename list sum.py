list1=[]
list2=[]
sum1=0
sum2=0
n1=int(input("Enter the limit of 1st list : "))
print("Enter the values of 1st list : ")
for i in range(0,n1):
    val1=int(input()) #inputting list1 items
    list1.append(val1)
    sum1=sum1+list1[i] #adding elements of list1
n2=int(input("Enter the limit of 2nd list : "))
print("Enter the values of 2nd list : ")
for i in range(0,n2):
    val2=int(input()) #inputting list2 items
    list2.append(val2)
    sum2=sum2+list2[i] #adding elements of list2
print("List1 :",list1)
print("List2 :",list2)
if(sum1==sum2): #condition of check sums of both lists
    print("List1 and List2 sums up to same value")
    print("Sum of both lists : ",sum1) #if yes, print the sum
else:
    print("list1 and List2 doesn't sum up to same value")
    print("Sum of 1st List:",sum1) #if no, print the sum of both lists
    print("Sum of 2nd List:",sum2)


