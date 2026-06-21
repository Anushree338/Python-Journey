#can you change the self parameter inside a class to something else(say "harry"), try changing 
#self to slf and harry and see effects
#write a class train whic has methods to book a ticket, get staus and get fare information of train running underIndian Railways
from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(harry, fro , to):
        print(f"Ticket is bboked in train no: {harry.trainNo} from {fro} to{to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro , to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")

#no change