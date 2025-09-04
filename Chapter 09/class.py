class Employee: 
    language = "Python" # class attribute
    salary = 120000


vinay = Employee()
vinay.name = "Vinay" # instance/object attribute
print(vinay.name, vinay.language, vinay.salary)

virat = Employee()
virat.name = "Virat"
print(virat.name, virat.salary, virat.language)


#? instance vs class attributes

ABD = Employee()
ABD.language = "JavaScript" 
print(ABD.language, ABD.salary) #! return "JavaScript", instance attributes are first priorty