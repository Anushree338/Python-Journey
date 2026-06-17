#write a program to read a text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'

f = open("poem.txt")
content= f.read()
if("twinkle" in content):
    print("Thw word twinkle is present in the content")
else:
    print("The word twinkle is not present in the content")
    
f.close()