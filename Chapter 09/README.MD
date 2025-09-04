# 📘 Chapter 09 – Object-Oriented Programming (OOPs)

Object-Oriented Programming (OOP) helps us model real-world problems using classes and objects.

---

## 1. Class & Object

- Class → Blueprint or template for creating objects
- Object → Instance of a class

```python
class Car:
    pass

my_car = Car()  # object creation
```

---

## 2. Modelling Problem in OOPs

- Identify entities as classes
- Identify attributes and behaviors as instance variables and methods

- Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age

```

---

## 3. Class Attributes vs Instance Attributes

- Class Attribute → Shared by all objects

```python
class Dog:
    species = "Canine"  # class attribute
```

- Instance Attribute → Unique for each object

```python
dog1 = Dog()
dog1.name = "Buddy"  # instance attribute
```
---

# 4. self Parameter

- Refers to the current object
- Used to access instance attributes and methods

```python
class Person:
    def __init__(self, name):
        self.name = name
```
---

## 5. Static Method

- Method that doesn’t access instance or class attributes
- Use @staticmethod decorator

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 7))
```
---

## 6. __init__ Constructor

- Special method called automatically when creating an object
- Used to initialize instance attributes

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Alice", 20)
print(s1.name, s1.age)
```
---

# ✅ Key Takeaways

- Class = Blueprint | Object = Instance
- Class attributes = shared | Instance attributes = unique
- self = current object
- Static method = independent of object
- __init__ = initializes object