def calculator(a, b, operation):
    print("Operation:", operation, "on", a, "and", b)
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"
print("Result:", calculator(10, 5, "+"))
print("Calculation done.")
print("---------------------------")
