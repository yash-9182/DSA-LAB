def is_palindrome(s):
    print("Checking if", s, "is palindrome")
    return s == s[::-1]
word = "madam"
print("Is Palindrome:", is_palindrome(word))
print("---------------------------")
