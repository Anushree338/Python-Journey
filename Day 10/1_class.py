class Employee:
    language = "Hindi"  #this is class atrribute
    salary = 1200000

anushree = Employee()
anushree.name = "Anushree"   #this is instance attribute
print(anushree.name, anushree.language, anushree.salary)

rohan = Employee()
rohan.name = "Robinsons"
print(rohan.name, rohan.language, rohan.salary)

#here name is instance attribute whereas salary and language are class attribute as they directly belong to class
