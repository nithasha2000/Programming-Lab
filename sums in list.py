a=int(input("Enter the limit : "))
l=[]
sum=0
print("Enter the elements in the list : ")
for i in range(a):
   a=int(input())
   l.append(a)  #appending each element to the list
   sum=sum+l[i] #adding each element as appending to the list
print("List :",l)
print("Sum of elements in the list =",sum)
