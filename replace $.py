s1=input("Enter a string : ") #user input string
s2=s1[0] #storing 1st letter
s3=s1[1:] #slicing string from the 2nd position
s4=s3.replace(s2,'$') # replacing the 1st string with $ in all occurences
replaced=s2+s4
print("The new string :",replaced)