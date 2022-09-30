length = int(input("length"))
count=0
num_arr=[]

for i in range(length):
    num_arr.append(int(input("Enter number "+str(i+1)+ ": ")))

for i in range(length-1):
    if num_arr[i]%2==0 and num_arr[i+1]%2==0:
        count=count+1
print(count)