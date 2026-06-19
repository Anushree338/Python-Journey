#repeat the question 4 for more sensored words

words = ["donkey", "bad", "ganda"]

with open("filee.txt", "r") as f:
    content = f.read()


for word in words:
    content = content.replace(word, "#" *len(word))

with open("filee.txt", "w") as f:
    f.write(content)