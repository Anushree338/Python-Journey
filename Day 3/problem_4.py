#replace double space with single space in the string

name = "Harry is a  good  boy   "

print(name.replace("  ", " "))  #replace double space with single space
print(name) #strings are immutable , original string will not change unless we assign it to a new variable or the same variable