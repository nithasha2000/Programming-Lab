num1 = int(input("Enter the number1 : ")) #input num1,num2,num3
num2 = int(input("Enter the number2 : "))
num3 = int(input("Enter the number2 : "))
if num1>num2 and num1>num3: #check whether num1 greater than num2 and num3
    print(num1,"is greatest ")
elif num2>num1 and num2>num3: #else, check whether num2 greater than num1 and num3
    print(num2,"is greatest")
else: #else num3 is greatest
    print(num3,"is greatest")