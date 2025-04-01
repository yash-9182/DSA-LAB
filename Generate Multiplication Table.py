def multiplication_table(num):
    print("Multiplication Table for:", num)
    table = []
    for i in range(1, 11):
        table.append(f"{num} x {i} = {num * i}")
    return table
print("\n".join(multiplication_table(3)))
print("Table generated.")
print("---------------------------")
