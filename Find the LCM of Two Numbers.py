def lcm(a, b):
    print("Finding LCM of:", a, "and", b)
    return (a * b) // gcd(a, b)
print("LCM:", lcm(12, 15))
print("---------------------------")
