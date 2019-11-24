''''sw=list()
for i in range(0,5,1):
    sw.insert(i,int(input()) )#insert 位置，目标
print(sw)
print(sw[3])
'''
deck=[x for x in range(52)]

#creat suits,ranks
suits=["Spades","Hearts","Diamonds","Clubs"]
ranks=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

import random
random.shuffle(deck)
for i in range(4):
    suit=suits[deck[i]//13]
    rank=ranks[deck[i]%13]
    print("card number",deck[i],"is the",rank,"of",suit)
