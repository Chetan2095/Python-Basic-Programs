n = int(input("Enter a number :"))
fact = 1
if n < 0:
    print("Factorial of negative number can not be calculated.")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n+1):
        fact = fact * i
    print("The factorial of", n, "is", fact)