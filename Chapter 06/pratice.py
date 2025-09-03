
#? Q1. Check Even / Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


#? Q2. Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest is:", a)
elif b > c:
    print("Largest is:", b)
else:
    print("Largest is:", c)

#? Q3. Print 1 to 10 using for loop
for i in range(1, 11):
    print(i)

#? Q4. Sum of 1 to 100 using while loop
i = 1

total = 0
while i <= 100:
    total += i
    i += 1
print("Sum is:", total)

#? Q5. Skip number 5 using continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#? Q6. Stop loop at 7 using break
for i in range(1, 11):
    if i == 7:
        break
    print(i)

#? Q7. Simple Guessing Game
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct! 🎉")
    else:
        print("Try again!")
