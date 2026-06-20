class Employee:
    language = "Hindi"  #this is class atrribute
    salary = 1200000

    def __init__(self):  #dunder method which is automatically called
        print("I m a coder")

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good morning")

harry = Employee()
harry.name = "Harry"
print(harry.name, harry.salary)
