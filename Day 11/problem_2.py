#create class pets from a class animals and further create a class dog from pets. add a method bark  to class dog

class Animals():
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow!")

d = Dog()
d.bark()
