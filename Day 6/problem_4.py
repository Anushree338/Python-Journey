#write program to find whether a given username contains less than 5 characters
username = input("Enter your name: ")

if(len(username)<=10):
    print("this username has lass than 10 characters")

else:
    print("All is well!")