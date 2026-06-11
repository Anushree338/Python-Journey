p1= "make a lot of money"
p2= "subscribe this"
p3= "buy now"
p4= "click this"

message= input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("This is scam")

else:
    print("This is not a scam")