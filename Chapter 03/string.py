name = "Vinay"

short = name[0:3] # start from 0 all the way till 3 (excluding 3)
print(short)
character1 = name[1]
print(character1)

#? Negative slicing

print(name[-4: -1])
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

#? Escape squence
a = 'Learning python : \n\'web development\' and \'Machine learning\''
print(a)