l=['amal','akash','bharath','divin','rakesh'] #list of names
c=0
print("List of names are : ")
for i in l:
    print(i) #printing names
print("\r")
for i in l:
    if 'a' in i: #condition to check a in each name
        c+=i.count('a') #if present, increment c
print("Occurrences of a in names are",c)