list=[-1,0,2,5,-8,17,-9] #list of integers
print("The list is ",list) #printing the list
newlist=[i for i in list if i>0] #checking each element in list is positive or not
print("Positive list : ",newlist) #newlist with positive integers