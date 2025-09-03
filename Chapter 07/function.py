
#? Function Definition
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    
    average = (a + b + c)/3
    print(f" The average of numbers : {average}")


avg() # Function Call

#? Function with arguments
def greet(name):
    print("Hello," + name)

greet("Vinay") 

#? Deafult arguments
def greet(name = "Unkown"):
    print("Hello," + name)

greet("Virat") 
greet() 

#? Function with return statement
def sum(a = 2, b = 3):
    return a+b

res = sum(10 ,20)
print(res)
