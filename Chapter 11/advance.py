from typing import List, Tuple, Dict, Union

#? Using Walrus Opreator
if(n := len([1,2,3,4])) > 3:
    print(f"List is too long, {n} elements")

#? Type defintions
num : int = 5  #! mentioning num type

#? Type Hints

numbers : List[int] = [1,2,3,4,5]
person: Tuple[str, int] = ("Vinay", 21)
cgpa : Dict[str, int] = {"vinay": 8.1, "virat": 9}

#? Match Case - similar to switch case

def http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server error"
        case _:
            return "unknown status"
        
print(http_status(200))

#? dictionary merge

dict1 = {'a': 1, "b" : 2}
dict2 = {'c': 3, "d" : 4}
merged = dict1 | dict2
print(merged)

#? Exception handling
try:
    age = int(input("Enter your age : "))
    print(age)

except Exception as e:
    print(e)

else:
    print("Everything good!") #! Runs only if try block runs

finally:
    print("Finished Excuation") #! Runs irrespective of result

#? enumerate
for ind, number in enumerate(numbers):
    print(f"The item number at index {ind} is {number}")
