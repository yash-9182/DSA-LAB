def gcd(a, b):
    print("Finding GCD of:", a, "and", b)
    while b:
        a, b = b, a % b
    return a
print("GCD:", gcd(48, 18))
print("---------------------------")
