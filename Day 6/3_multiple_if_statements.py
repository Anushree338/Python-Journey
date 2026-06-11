a = int(input("Enter your age: "))

#statement 1 runs independently
if(a%2 ==0):
    print("Your age is even")

#statement 2

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<18):
    print("You are entering an invalid age")

elif(a==0):
    print("You are enetring 0 which is not valid")

else:
    print("You are below the age of consent")

print("End of program")