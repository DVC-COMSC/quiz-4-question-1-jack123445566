length=int(input("Enter the length of the sequence: "))
count=0
num1=int(input("Enter number "+str(1)+ ": "))
for i in range(length-1):
    num2=int(input("Enter number "+str(i+2)+ ": "))
    if((num1%2==0) and (num2%2==0)):
        count=count+1
    num1=num2
print("The number of pairs of adjacent even numbers is "+ str(count))
