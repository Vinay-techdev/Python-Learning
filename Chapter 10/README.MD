# 📘 Chapter 10 – Object-Oriented Programming (OOPs) – Inheritance & Advanced Concepts

Inheritance allows a class (child class) to inherit properties and methods from another class (parent class). This helps in code reusability and creating a logical structure for programs.

---

# Types of Inheritance

 1. Single Inheritance
  - One child class inherits from one parent class.

 2. Multiple Inheritance
  - A class inherits from more than one parent class.

 3. Multilevel Inheritance
  - A child class inherits from a parent class, which itself inherits from another parent class (grandparent).

 4. Hierarchical Inheritance
  - Multiple child classes inherit from a single parent class.

---

# Key Concepts

 **super() Method**
    Used to call the parent class constructor or methods from the child class.

 **Class Method**
    Defined using @classmethod, it takes cls as the first argument instead of self.
    Used for creating factory methods or modifying class-level attributes.

 **Property Decorator**
   Allows defining getter, setter, and deleter methods in a Pythonic way to access attributes like properties.

---

# Operator Overloading

Python allows redefining how operators work for custom classes by using special methods (dunder methods).

| Operator | Method Name      | Example        |
| -------- | ---------------- | -------------- |
| `+`      | `__add__()`      | `obj1 + obj2`  |
| `-`      | `__sub__()`      | `obj1 - obj2`  |
| `*`      | `__mul__()`      | `obj1 * obj2`  |
| `/`      | `__truediv__()`  | `obj1 / obj2`  |
| `//`     | `__floordiv__()` | `obj1 // obj2` |
| `len()`  | `__len__()`      | `len(obj)`     |
| `str()`  | `__str__()`      | `print(obj)`   |

---

# ✅ Key Takeaways 

- Learned different types of inheritance (single, multiple, multilevel, hierarchical) and how to use super() for reusing parent class methods.
- Explored class methods, property decorators, and setters to manage class data and attributes cleanly.
- Practiced operator overloading (__add__, __len__, etc.) to make custom classes behave like built-in types.