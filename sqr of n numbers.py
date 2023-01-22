n=int(input("Enter a number to which square should be calculated : ")) #user inputting limit
list=[]
for i in range(1,n+1): #adding list items to the list
    list.append(i)
print("The list of numbers are : ")
print(list) #printing list elements
print("The square of numbers in the above list are :")
newlist=[i**2 for i in list if i<n+1] #calculating square of each numbers using list comprehension
print(newlist)
