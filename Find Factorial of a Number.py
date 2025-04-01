def factorial(n):
    print("Finding factorial of:", n)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = 5
fact = factorial(num)
print("Factorial:", fact)
print("Factorial calculated.")
print("---------------------------")
