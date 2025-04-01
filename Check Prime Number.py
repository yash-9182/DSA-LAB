def is_prime(n):
    print("Checking if", n, "is prime")
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num = 11
prime_status = is_prime(num)
print("Is Prime:", prime_status)
print("Prime check done.")
print("---------------------------")
