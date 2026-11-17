def fibbonacci(n):
    a = 0
    b = 1
    #c = a + b
    for i in range(n):
        print(a, end=" ")
        c=a+b
        a = b
        b = c
n=int(input("enter the number of terms: "))
fibbonacci(n)
#print("fibbonacci series:")