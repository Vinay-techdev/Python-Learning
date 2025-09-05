def fun():
    print("Hello world!")

# fun()
# print(__name__) #if we run main folder it will show output - Hello world!

if __name__ == "__main__":
    #! If this code is directly executed by running the file its present(module.py) in then print following
    print("Codes are from main module")

    fun()
    print(__name__) 