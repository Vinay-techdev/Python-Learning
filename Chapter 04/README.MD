# 📖 Chapter 04 – Python Lists & Tuples

This chapter introduces lists and tuples, two essential collection types in Python.

---

# 🖥️ Topics Covered

# 1. Lists (Mutable)

Lists are ordered, changeable collections that can hold multiple data types.

- Indexing : Access elements by their position (index)
- Slicing : Extract sub-lists using slicing

---

# Common List Methods :

| Method      | Description                            | Example                   |
| ----------- | -------------------------------------- | ------------------------- |
| `append()`  | Add element at the end                 | `my_list.append(99)`      |
| `insert()`  | Insert element at a specific index     | `my_list.insert(2,"Hi")`  |
| `remove()`  | Remove first matching element          | `my_list.remove(2)`       |
| `pop()`     | Remove element at index (default last) | `my_list.pop()`           |
| `sort()`    | Sort the list (ascending)              | `numbers.sort()`          |
| `reverse()` | Reverse the list                       | `my_list.reverse()`       |
| `count()`   | Count occurrences of an element        | `my_list.count(3)`        |
| `index()`   | Find index of an element               | `my_list.index("Python")` |

---

# 2. Tuples (Immutable)

Tuples are ordered, unchangeable collections.

- Indexing : Access elements using index (same as lists)
- Slicing : Extract sub-tuples using slicing

--- 

# Common Tuple Methods :

| Method    | Description                          | Example                    |
| --------- | ------------------------------------ | -------------------------- |
| `count()` | Count occurrences of an element      | `my_tuple.count(3)`        |
| `index()` | Find index of first matching element | `my_tuple.index("Python")` |

- 💡 Note: Tuples are immutable, so methods like append(), remove(), or sort() cannot be used.

---

3. Mini Challenge

- Take a list of numbers from the user (comma-separated).
- Convert it to a tuple.
- Print:
  1. Sorted list
  2. Maximum & minimum value
  3. Count of a specific number entered by user

---

# 💡 Key Takeaways

- Lists are mutable — you can add, remove, and modify elements.
- Tuples are immutable — elements cannot be changed once created.
- Both support indexing, slicing, and functions like count() and index().
- Choosing between list and tuple depends on whether you need modifiability or fixed data.