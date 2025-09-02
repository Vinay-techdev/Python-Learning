# Dictionary Practice
person = {"name": "Vinay", "age": 30, "city": "Davangere"}
print(person["name"])
person["age"] = 31
person["job"] = "Engineer"
print(person.keys())
print(person.values())
print(person.items())
person.pop("city")
print(person)

# Set Practice
numbers = {1, 2, 3, 4, 4, 5}  # duplicates removed
numbers.add(6)
numbers.remove(2)
print(numbers)
print(len(numbers))
print(3 in numbers)

# Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference:", set_a.difference(set_b))
