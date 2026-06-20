class Employee:
    language = "Hindi"  #this is class atrribute
    salary = 1200000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good morning")

harry = Employee()
harry.greet()
harry.getinfo()
