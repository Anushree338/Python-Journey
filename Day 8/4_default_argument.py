def goodDay(name, ending= "Thank you"):  #same take default value
    print(f"Good day, {name}")
    print(ending)

goodDay("Harry")
# output:
'''
Good day, Harry
Thank you
'''

def goodDay(name, ending):
    print(f"Good day, {name}")
    print(ending)

goodDay("Harry", "Thanks")  #otherwise take this value