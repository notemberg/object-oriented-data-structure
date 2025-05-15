def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)

number = 5
print(f"Factorial of {number} is {factorial(number)}")