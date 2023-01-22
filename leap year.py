cyear=int(input("Enter the current year : ")) #current year
fyear=int(input("Enter a future year to calculate leap year : ")) #future year
print("Leap years between ",cyear," and ",fyear," are :") #print statement printing the user input years
for i in range(cyear,fyear): #checking whether each year within the loop is leap year or not
    if(i%400==0) or (i%4==0 and i%100!=0):
        print(i)
