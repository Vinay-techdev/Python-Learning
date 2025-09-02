my_dict = {'name': 'vinay', 'age': 25}

print(my_dict.keys()) 
print(my_dict.values())
print(my_dict.items())

#? Returns the value for a key. If the key doesn’t exist, returns default instead of error.
print(my_dict.get('name')) 
print(my_dict.get('gender', 'N/A')) #! Default 'N/A'

#? Updates the dictionary with key-value pairs from another dictionary.
my_dict.update({'age': 26, 'gender': 'Male'})
print(my_dict)  # Output: {'name': 'Vinat', 'age': 21, 'gender': 'Female'}

#? Removes the key and returns its value.
age = my_dict.pop('age')
print(age)      # Output: 21
print(my_dict)

#? Removes and returns the last inserted key-value pair as a tuple.
age = my_dict.pop('age')
print(age)    
print(my_dict)

my_dict.clear()
print(my_dict)

my_dict = {'name': 'vinay', 'age': 25}
new_dict = my_dict.copy()
print(new_dict)

# --------------------------------------
# 💡 Extra notes:

#? You can check if a key exists:
'name' in my_dict  #! True
'city' in my_dict  #! False

#? Iterating through dictionary:
for key, value in my_dict.items():
    print(key, value)
