
#? class method
class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45 #! if we do not mention @classmethod its show 45 bcz instance attributes are 1st priroty

e.show()


#? proprty decorator
class Employee:
    a = 1

    def show(cls):
        print(f"The class attribute of a is {cls.a}")
    
    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45 #! print 45 bcz we do not mention @classmethod and instance attributes are 1st priroty

e.name = "Vinay P"
print(e.fname, e.lname)

e.show()

#? Operator overloading
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)