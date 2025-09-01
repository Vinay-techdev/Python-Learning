my_list = [1, 2, 3]

my_list.append(4)
print(my_list)

my_list.extend([5, 6])
print(my_list)

my_list.insert(1, 2.0)
print(my_list)

my_list.remove(2)
print(my_list)

popped = my_list.pop()
print(popped)  
print(my_list)

my_list = [1, 2, 3]
my_list.clear()
print(my_list) 

my_list = [1, 2, 3, 2]
print(my_list.index(2)) 

my_list = [1, 2, 2, 3]
print(my_list.count(2))

my_list = [3, 1, 2]
my_list.sort()
print(my_list) 

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)

my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)