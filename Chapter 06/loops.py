print(1)
print(2)
print(3)
print(4)
print(5)

# The same task can be done like this:
#? Foor loop
for i in range(1, 6):
    print(i)

## For Loop with Lists
l = [1, 2,3,4,5,6]
for i in l:
    print(i)

## For Loop with Tuples
t = (63, 31, 5, 22)
for i in t:
    print(i)

## For Loop with Strings
s = "Vinay"
for i in s:
    print(i)

## For Loop with else
l= [1,7,8] 

for iii in l:
    print(iii)

else:
    print("done") # this is printed when the loop ends

#? while loop
i = 1

while(i<10):
    print(i)
    i +=1 # or i = i + 1

#? Break and Coniue

for i in range(10):
    if(i == 4):
        break # Exit the loop right now
    print(i)

for i in range(10):
    if(i == 4):
        continue # Skip this iteration
    print(i)    