# s = {1, 2, 3} # set of integers


e = set() # empty set, dont use s = {} because it creates an empty dictionary
s = {1, 2, 3, 4, 5, 5 , 5 ,5, "Harry"} # set of integers, duplicates are automatically removed
print(s, type(s)) # output: {1, 2, 3, 4, 5, 'Harry'} <class 'set'>

s.add(6) # add an element to the set
print(s) 

s.remove(3) # remove an element from the set, if element is not present it raises an error
print(s, type(s))