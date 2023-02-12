s=input("Enter strings : ")
s=s.split(",")
a=[]
for i in s:
    a.append(i) #appending strings to list

max = len(a[0]) #storing length of 1st string in max
temp = a[0] #storing 1st string in temp

for i in a:
    if(len(i) > max): #checking length of each word
        max = len(i)
        temp = i

print("The word with the longest length is:", temp,"and length is ", max)