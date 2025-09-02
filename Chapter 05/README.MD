# 📖 Chapter 06 – Python Dictionaries & Sets

This chapter introduces Dictionaries (mutable) and Sets (immutable collections) in Python.

---

# 🖥️ Topics Covered

# 1. Dictionaries (Mutable)

- Dictionaries store data in key-value pairs.
- Accessing & Indexing : Use keys to access values
- Modifying : Update existing keys or add new ones

---

# Common Dictionary Methods

| Method     | Description                       | Example              |
| ---------- | --------------------------------- | -------------------- |
| `keys()`   | Returns all keys                  | `person.keys()`      |
| `values()` | Returns all values                | `person.values()`    |
| `items()`  | Returns key-value pairs           | `person.items()`     |
| `pop()`    | Removes key and returns its value | `person.pop("city")` |
| `clear()`  | Removes all items                 | `person.clear()`     |

---

# Dictionary Practice Explanation:

- Create a dictionary with keys like name, age, city.
- Access values using keys, update existing ones, or add new keys.
- Use keys(), values(), items() to see all keys, values, or key-value pairs.
- pop() removes a key from the dictionary

--- 

# 2. Sets (Immutable Elements)

- Sets are unordered collections of unique elements.
- Accessing : Sets do not support indexing, but you can iterate

---

# Common Dictionary Methods

| Method           | Description                           | Example                   |
| ---------------- | ------------------------------------- | ------------------------- |
| `add()`          | Adds an element                       | `numbers.add(6)`          |
| `remove()`       | Removes an element (error if missing) | `numbers.remove(2)`       |
| `discard()`      | Removes element (no error if missing) | `numbers.discard(10)`     |
| `union()`        | Returns union of sets                 | `set1.union(set2)`        |
| `intersection()` | Returns intersection of sets          | `set1.intersection(set2)` |
| `difference()`   | Returns difference of sets            | `set1.difference(set2)`   |
| `len()`          | Returns number of elements            | `len(numbers)`            |
| `in`             | Checks membership                     | `3 in numbers`            |

---

# Set Practice

- Sets store unique elements (duplicates are removed automatically).
- Use add() to add elements, remove() to delete, len() for size, and in to check if an element exists.

---

# Set Operations

- Union → combines all elements from two sets.
- Intersection → keeps only common elements.
- Difference → elements in the first set but not in the second.

---

# 💡 Key Takeaways

- Dictionaries are mutable and ideal for key-value data storage.
- Sets store unique, unordered elements; useful for removing duplicates or performing set operations.
- Dictionaries support key-based access, while sets do not support indexing.
- Both have built-in methods for manipulating and querying data efficiently.