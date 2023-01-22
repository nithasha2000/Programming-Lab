s1=input("Enter a string : ") #input string
s2=s1[0] #storing 1st char
s3=s1[-1] #storing last char
s4=s1.replace(s2,s3) #replacing 1st char with last char
s5=s4[0] #storing 1st char of replaced string
s6=s4[1:] #slicing string from 2nd position
s7=s6.replace(s3,s2) #replacing last char with 1st char of old string
s8=s5+s7 #concatenate both results s5 and s7
print("New string :",s8)