#write a program to greet all the persons name stored in a list l and which starts with S 

l = ["Harry", "Sejal", "Swara", "Parth", "Anuu"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
