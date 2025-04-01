def count_vowels(s):
    print("Counting vowels in:", s)
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
text = "Hello World"
print("Vowel Count:", count_vowels(text))
print("---------------------------")
