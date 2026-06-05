#write a program to detect double spaces in a string 

name = "Harry is a good boy"

print(name.find("  "))  #return -1 if no double space 

name = "Harry is a  bad  boy"

print(name.find("  "))  #return the index of the first occurrence of double space