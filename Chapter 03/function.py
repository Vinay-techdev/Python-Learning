name = "hey, i am vinay"

print(len(name))
print(name.endswith("nay"))
print(name.startswith("hey"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.title()) #? Capitalizes the first letter of each word.
print(name.strip()) #? Removes leading and trailing whitespace (or other specified characters).

print(name.replace("vinay", "vinnu"))
print(name.split(", "))
print(name.find("vinay"))
print(name.count("vinay")) #? Counts how many times a substring appears.