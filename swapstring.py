a=input("Enter a atring : ")
b=input("Enter another string : ")
str1=b[0]+a[1:] #adding 1st char of 2nd string to 1st string
str2=a[0]+b[1:] #adding 1st char of 1st string to 2nd string
print("Modified string : ",str1+" "+str2)