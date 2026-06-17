#a file contains a word "donkey" multiple times. you need to write a program to replace this word with ### by updating the same file
word = "donkey"

with open("filee.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "####")

with open("filee.txt", "w") as f:
    f.write(contentNew)