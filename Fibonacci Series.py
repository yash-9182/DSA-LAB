def fibonacci(n):
    print("Generating Fibonacci series up to:", n)
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
print("Fibonacci Series:", fibonacci(10))
print("---------------------------")
