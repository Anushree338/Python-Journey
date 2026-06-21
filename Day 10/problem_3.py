#create a class with a class attribute a, create an object from it and set 'a' directly using object.a = o
#does this change the class attribute

class Demo:
    a = 4

o = Demo()
print(o.a) #prints class attribute becuase instance attribute is not presentt

o.a = 0
print(o.a)  #prints instance attribute beacause it is present 

print(Demo.a)  #prints class attribute 

#no it does not change 