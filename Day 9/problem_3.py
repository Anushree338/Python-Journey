#write a program to generate multiplication table from 2 to 20 and write it to the different files. place this file in a folder of 13 yr old

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} * {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)