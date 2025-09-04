
#! Writing file
data = "Vinay - A full stack developer"
#? Opening file
f = open("file.txt", "a") # defining write mode("w")
 
print(f.write(data))

#? Closing file
f.close()

#! Appending content at end of file
dataApp = '''\n\nA passionate full stack developer who loves building interactive user interfaces and scalable backend APIs. 
I focus on writing clean, efficient code and continuously learning modern technologies.'''

#? Opening file
f = open("file.txt", "a")
 
print(f.write(dataApp))

#? Closing file
f.close()


#! Reading file
f = open("file.txt") 
 
print(f.read())

f.close()


#! Reading file - line by line
f = open("file.txt")
print(f.readline())
print(f.readline())

f.close()


#! Reading file - line by line at once and store it in list
f = open("file.txt")
 
print(f.readlines())

f.close()

#! With statement - we do not need to close file manulay everytime
with open("file.txt") as f:
    print(f.read())