
#? Q1. Function to print "Good Morning"
def good_morning():
    print("Good Morning!")

good_morning()

#? Q2. Function to add two numbers
def add(a, b):
    return a + b

print(add(5, 7))

#? Q3. Function to find square of a number
def square(num):
    return num ** 2

print(square(6))

#? Q4. Recursive function to print numbers 1 to 5
def print_numbers(n):
    if n > 5:
        return
    print(n)
    print_numbers(n + 1)

print_numbers(1)
