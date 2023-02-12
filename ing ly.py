s=input("Enter the string : ")
if s[-3:]=="ing": #checking whether string ends with 'ing'
	print(" Modified string = ",s+"ly") #if yes, add 'ly'
else:
	print("Modified string = ",s+"ing") #else add 'ing'
