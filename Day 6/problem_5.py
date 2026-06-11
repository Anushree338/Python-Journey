#write a program to find out whether given name is present or not

l = ["Harry" , "Anushree" , "Jiny" , "Madhuri"]

name = input("Enter your name: ")

if(name in l):
    print("You are in a list")

else:
    print("You are not in a list")