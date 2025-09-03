a = int(input("Enter your age: "))

# If statement
if(a%2 == 0):
    print("a is even")

# If else statement
if(a>=18):
    print("You are eligible")
    print("Good for you")
else:
    print("You are below the age")

b = int(input("Enter your age: "))

# If elif else ladder
if(b>=21):
    print("You are above the age")
    print("Good for you")

elif(b<0):
    print("Enter valid age")

elif(a==0):
    print("0 is not age")    

else:
    print("You are below the age")

print("End of Program")