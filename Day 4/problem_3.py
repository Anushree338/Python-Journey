#check that tuple type cannot be changed in python

a = (1,23,45,666, "Rohan", True)
a[2] = 100  #this will give an error because tuples are immutable
print(a)