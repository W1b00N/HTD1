n = int(input("Enter a number: "))
while n >= 1:
    for i in range(1, n+1):
        print(i, end=" ")
    print("")
    n = n - 1