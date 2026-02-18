#Stars
a = int(input("Enter the number of rows: "))
for i in range(a+1):
    print('*'*(i))

a = int(input("Enter the number of rows: "))
for i in range(a+1):
    print(" "*(a-i), end ="")
    print("*" * i)

a = int(input("Enter the number of rows: "))
for i in range(a):
    print("*"*(a))

a = int(input("Enter the number of rows: "))
for i in range(a+1):
    print(" "*(a-i), end="")
    print("*" * (2*i-1))

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    if i == 1 or i == n:
        print("*"*(n), end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")
