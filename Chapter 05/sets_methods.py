my_set = {1, 2, 3}

my_set.add(4)
print(my_set)   # Output: {1, 2, 3, 4}

my_set.update([5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5, 6}

my_set.discard(10)  #? Removes an element if it exists. No error if element doesn’t exist.

#? Removes and returns a random element (since sets are unordered).
elem = my_set.pop()
print(elem)     # Output: could be any element
print(my_set)

my_set.clear()
print(my_set)  # Output: set()

#? Returns a new set containing all elements from both sets.
s1 = {1, 2}
s2 = {2, 3}
print(s1.union(s2))  # Output: {1, 2, 3}
print(s1 | s2)       # Same as union

#? Returns a set of elements common to both sets.
print(s1.intersection(s2))  # Output: {2}
print(s1 & s2)              # Same as intersection

#? Returns elements in the first set not in the second.
print(s1.difference(s2))  # Output: {1}
print(s1 - s2)             # Same as difference

#? Returns elements in either set but not in both.
print(s1.symmetric_difference(s2))  # Output: {1, 3}
print(s1 ^ s2)                       # Same as symmetric_difference

#? Checks if all elements of the set are in another set.
s1 = {1, 2}
s2 = {1, 2, 3}
print(s1.issubset(s2))  # True

#? Checks if the set contains all elements of another set.
print(s2.issuperset(s1))  # True