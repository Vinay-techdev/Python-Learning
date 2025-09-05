# **Chapter 11 – New Python Features & Concepts** 🚀

In this chapter, I explored some **newly introduced Python features** and important concepts to write cleaner, modern, and more maintainable code.

---

## **1. Walrus Operator (`:=`)**

* Introduced in **Python 3.8**.
* Allows assignment and expression evaluation in a single line.

```python
# Example
if (n := len([1, 2, 3])) > 2:
    print(f"List has {n} elements")
```

---

## **2. Type Definitions & Type Hints**

* Helps define expected data types for variables and function arguments.
* Makes code **self-documenting** and easier to understand.

```python
age: int = 21

def greet(name: str) -> str:
    return f"Hello {name}"
```

---

## **3. Match-Case (Structural Pattern Matching)**

* Introduced in **Python 3.10**.
* Works like a `switch-case` in other languages.

```python
command = "start"

match command:
    case "start":
        print("System Starting...")
    case "stop":
        print("System Stopping...")
    case _:
        print("Unknown Command")
```

---

## **4. Dictionary Merge & Update Operators**

* Python 3.9 introduced `|` (merge) and `|=` (update).

```python
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

print(a | b)   # {'x': 1, 'y': 3, 'z': 4}
a |= b         # Updates a with b
```

---

## **5. Exception Handling**

* Handle errors gracefully using `try-except`.

```python
try:
    num = int("abc")
except ValueError:
    print("Invalid number!")
```

---

## **6. `__main__`**

* Special variable that allows code execution only when the file is run directly, not imported.

```python
if __name__ == "__main__":
    print("This runs only when file is executed directly.")
```

---

## **7. Global Variables**

* Use `global` keyword to modify a variable outside the current scope.

```python
count = 0

def increment():
    global count
    count += 1
```

---

## **8. Enumerate**

* Adds counter/index while iterating through iterable.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

---

Got it! Here’s a **clean table** + **key takeaways** for Chapter 11:

---

## **Feature Table**

| **Feature**                | **Explanation**                              | **Example**                                    |                                    |              |     |
| -------------------------- | -------------------------------------------- | ---------------------------------------------- | ---------------------------------- | ------------ | --- |
| **Walrus Operator (`:=`)** | Assigns value & checks condition in one line | `if (n := len(data)) > 3: print(n)`            |                                    |              |     |
| **Type Hints**             | Adds expected data types for readability     | `def add(x: int, y: int) -> int: return x + y` |                                    |              |     |
| **Match-Case**             | Python's version of `switch-case`            | `match x: case 1: print("One")`                |                                    |              |     |
| \*\*Dict Merge (\`         | `) & Update (`                               | =\`)\*\*                                       | Merge & update dictionaries easily | \`merged = a | b\` |
| **Exception Handling**     | Catches errors to prevent crashes            | `try: ... except: ...`                         |                                    |              |     |
| **`__main__`**             | Runs code only if file is executed directly  | `if __name__ == "__main__": ...`               |                                    |              |     |
| **Global Variables**       | Modify variables outside function scope      | `global count`                                 |                                    |              |     |
| **Enumerate**              | Iterate with index & value                   | `for i,v in enumerate(lst): ...`               |                                    |              |     |

---

## **Key Takeaways** ✅

* 🆕 Learned **modern Python features** like walrus operator, match-case, and dictionary merging.
* 📖 Started using **type hints** for clean & maintainable code.
* 🛠 Improved error handling with **try-except** blocks.
* 🧠 Learned best practices like `__main__` and `enumerate` for better program structure.
