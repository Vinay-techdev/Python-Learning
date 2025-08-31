# 📖 Chapter 02 – Python Variables & Basics

This chapter covers variables, data types, operators, and input in Python — the building blocks for writing Python programs.

---

# 🖥️ Topics Covered
1. Variables

- Variables are used to store data in memory for later use.

2. Rules for Variable Names

- Must start with a letter or underscore.
- Can only contain letters, numbers, and underscores.
- Cannot use Python reserved keywords.
- Variable names are case-sensitive.

3. Data Types - Python automatically assigns a data type when a variable is created.

Common types:

- int → integers, e.g., 10
- float → decimal numbers, e.g., 3.14
- str → string, e.g., "Hello"
- bool → True/False
- list, tuple, dict, set → collections (Cover it next chapter)

4. Check type using type():

``` bash
x = 10
print(type(x))  # <class 'int'>
```

5. Operators

- Operators are used to perform operations on variables.

6. User Input

- Use input() to take input from the user
- By default, input() returns a string, so type conversion is needed for numbers.

---

# 💡 Key Takeaways

- Variables store data and follow specific rules.
- Python has dynamic typing — you don’t need to declare type explicitly.
- Operators allow performing mathematical, logical, and comparison operations.
- input() allows interactive programs.
- Always check variable type with type() to avoid errors.