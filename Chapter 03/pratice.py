sentence = input("Enter a sentence: ")

clean = sentence.strip()
title_case = clean.title()
word_count = len(clean.split())
replaced = clean.replace("Python","Java")

print("Title Case:", title_case)
print("Word Count:", word_count)
print("After Replacement:", replaced)
