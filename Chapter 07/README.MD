# 📘 Chapter 07 – Functions & Recursion  

This chapter covers **functions** (to organize code into reusable blocks) and **recursion** (when a function calls itself).  

---

## 🧠 1. Functions  

Functions help in **breaking code into smaller, reusable parts**.  

---

### 🔹 Types of Functions  
1. **Built-in Functions** – Already available in Python  
   ```python
   print(len("Hello"))  # len() is a built-in function
   ```

2. **User-Defined Functions** – Created by us
   ```python
   def greet():
    print("Hello, welcome to Python!")
   ```

---

# 🔹 Function Definition & Call

``` python
def say_hello():         # Function definition
    print("Hello World")

say_hello()              # Function call

```

---

# 🔹 Function with Arguments

``` python
def greet_user(name):
    print(f"Hello, {name} 👋")

greet_user("Vinnu")
greet_user("John")

```
---

# 🔹 Function with Return
``` python
def add(a, b):
    return a + b

result = add(5, 10)
print("Sum:", result)

```
---

# 🔄 2. Recursion

Recursion = function calling itself until a condition is met.

---

# ✅ Quick Summary

| Concept               | Example                 |
| --------------------- | ----------------------- |
| Built-in Function     | `len("hello")`          |
| User-Defined Function | `def my_func(): ...`    |
| Arguments             | `def add(a, b): ...`    |
| Return                | `return value`          |
| Recursion             | Function calling itself |

---

# 🏋️ Practice Set
- Q1. Function to print "Good Morning"
- Q2. Function to add two numbers
- Q3. Function to find square of a number
- Q4. Recursive function to print numbers 1 to 5