#write a problem to accept marks of five subjects and store them in a list and print the list
marks = []

f1 = int(input("Enter marks 1: ")) #string hai isliye int me convert karna padta hai nhi toh sort nhi hoga
f2 = int(input("Enter marks 2: "))
f3 = int(input("Enter marks 3: "))
f4 = int(input("Enter marks 4: "))
f5 = int(input("Enter marks 5: "))
f6 = int(input("Enter marks 6: "))
f7 = int(input("Enter marks 7: "))

marks.append(f1)
marks.append(f2)
marks.append(f3)
marks.append(f4)
marks.append(f5)
marks.append(f6)
marks.append(f7)

marks.sort()  #sort the marks in ascending order

print(marks)