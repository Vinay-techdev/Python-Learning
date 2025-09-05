
#? Multi-level inheritance
class a:
    def __init__(self):
        print("Constructor of a")
    a = 1

class b(a):
    def __init__(self):
        #? super method
        super().__init__()
        print("Constructor of b") 
    b = 2

class c(b):
    def __init__(self):
        #? super method
        super().__init__()
        print("Constructor of c")
    c = 3


o = c()
print(o.a, o.b, o.c)