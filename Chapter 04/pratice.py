numbers = input("Enter numbers separated by comma: ").split(",")
numbers = [int(num) for num in numbers]
numbers_tuple = tuple(numbers)

print("Sorted List:", sorted(numbers))
print("Max:", max(numbers_tuple))
print("Min:", min(numbers_tuple))

num = int(input("Enter a number to count: "))
print(f"Count of {num}:", numbers_tuple.count(num))
