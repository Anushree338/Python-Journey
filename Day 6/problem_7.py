#program to find out whether a given post is about "harry" or not

post = input("Enter the post: ")

if("harry" in post.lower()):   #harry in any case lower or upper ex: harry or haRry
    print("This post is talking about Harry")

else:
    print("This post is not talking about Harry")