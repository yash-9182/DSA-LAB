def count_words(sentence):
    print("Counting words in:", sentence)
    return len(sentence.split())
sentence = "Python is a powerful programming language"
print("Word Count:", count_words(sentence))
print("---------------------------")
