class Employee: 
    language = "Python"
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
 

vinay = Employee("vinay", 1300000, "JavaScript") 
# harry.name = "Harry"
print(vinay.name, vinay.salary, vinay.language)
