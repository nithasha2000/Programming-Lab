s1=input("Enter the string : ")
s2=s1.split( ) #spilitting each word in the string
d={}
for i in s2:
    if i in d:
       d[i.lower()]+=1 #if word occurs more than once,increment
    else:
        d[i.lower()]=1 #if word occurs just once, assign 1
print(d)