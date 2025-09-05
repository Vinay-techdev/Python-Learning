
#? Single inheritance
class a:
    def show(slef):
      print("i am class a")

class b(a):
    def display(slef):
      print("i am class b")

obj = b()
obj.show()
obj.display()

#? multiple inheritance
class a:
    def show(slef):
      print("i am class a")

class b:
    def display(slef):
      print("i am class b")

class c(a,b):
   def pri(slef):
      print("i am class c")

obj = c()
obj.show()
obj.display()
obj.pri()