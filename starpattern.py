num=int(input("Enter the limit : "))
for i in range(1,num+1):    #star pattern 1
    for j in range(1,i+1):
        print("* ",end='')
    print("\n")
for i in range(num+1,0,-1):  #star pattern 2
    for j in range(1,i+1):
        print("* ",end='')
    print("\n")