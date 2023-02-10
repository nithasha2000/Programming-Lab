y = {'liya': 40,'alan': 2,'bob': 1,'danny': 3}  #adding key-value pair to dictionary
print("Dictionary : ",y)
l = list(y.items()) #converting to list
l.sort() #sorting in ascending order
print("Ascending order is ", l)
l.sort(reverse=True) #reversing the order
print("Descending order is ", l)