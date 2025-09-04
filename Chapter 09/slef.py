class Employee: 
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


vinay = Employee()
vinay.greet() # same as Employee.getInfo(harry)
vinay.getInfo() 
 