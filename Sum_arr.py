n=int(input("Enter a number of elements:"))
arr=[]
for i in range(0,n):
    x=int(input("Enter element:"))
    arr.append(x)
sum=0
for i in range(n):
    sum=sum+arr[i]
print("Sum =",sum)
