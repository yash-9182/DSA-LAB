def remove_duplicates(lst):
    print("Removing duplicates from:", lst)
    return list(set(lst))
numbers = [1, 2, 2, 3, 4, 4, 5]
print("Unique List:", remove_duplicates(numbers))
print("---------------------------")
