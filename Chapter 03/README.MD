# 📖 Chapter 03 – Python Strings & Functions

This chapter focuses on strings, indexing, slicing, and functions — essential tools for handling text in Python.

---

# 🖥️ Topics Covered

1. Strings

- Strings are sequences of characters enclosed in single ' ' or double " " quotes.

2. Indexing

- Each character in a string has a position (index) starting from 0.
- Access characters using square brackets [].

3. Slicing

- Extract a substring using start:stop format.

4. Negative Indexing & Slicing

- Negative indexes count from the end of the string (-1 is last character)

---

# Escape Sequences

- Special characters are represented using escape sequences:

| Escape | Meaning |
|--------|-----------------|
| \n | New line |
| \t | Tab |
| \\ | Backslash |
| \' | Single quote |
| \" | Double quote |

---
# String Functions / Methods

- Python provides many built-in methods for strings:

| Function / Method             | Description                           | Example                                       |
| ----------------------------- | ------------------------------------- | --------------------------------------------- |
| `len()`                       | Returns length of string              | `len("Python") → 6`                           |
| `upper()`                     | Converts string to uppercase          | `"python".upper() → "PYTHON"`                 |
| `lower()`                     | Converts string to lowercase          | `"PYTHON".lower() → "python"`                 |
| `capitalize()`                | Capitalizes first character           | `"python".capitalize() → "Python"`            |
| `title()`                     | Capitalizes first letter of each word | `"hello world".title() → "Hello World"`       |
| `strip()`                     | Removes leading/trailing whitespaces  | `"  hello  ".strip() → "hello"`               |
| `replace(old, new)`           | Replaces substring                    | `"hello".replace("h","H") → "Hello"`          |
| `split()`                     | Splits string into list               | `"a b c".split() → ['a','b','c']`             |
| `join()`                      | Joins list into string                | `" ".join(['Hello','World']) → "Hello World"` |
| `find()` / `index()`          | Finds position of substring           | `"Python".find("t") → 3`                      |
| `startswith()` / `endswith()` | Checks start/end of string            | `"Python".startswith("P") → True`             |

---

# Mini Challenge

- Ask the user to input a sentence.
- Perform the following:
   1. Remove extra spaces
   2. Convert to title case
   3. Count number of words
   4. Replace one word with another

---

# 💡 Key Takeaways

- Strings are sequences of characters that can be indexed and sliced.
- Negative indexing lets you access characters from the end.
- Escape sequences handle special characters.
- String methods allow you to manipulate, format, and query strings efficiently.
