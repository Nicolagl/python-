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
'''
from tkinter import *
import random
from PIL import Image, ImageTk
class deckcardgui:
    def __init__(self):
        window=Tk()#creat a win
        window.title("Pick 4 ")
        self.imageList=[ ]#store images for cards
        print("1")
        for i in range(1,53):
            self.imageList.append(ImageTk.PhotoImage(file="image/card/"+str(i)+".jpg"))
        frame=Frame(window)
        frame.pack()
       
        self.labelList=[ ]#a list of four labels
        print("2")
        for i in range(4):
            self.labelList.append(Label(frame,image=self.imageList[i]))
            self.labelList[i].pack(side = LEFT)
        print("3")
        Button(window,text="Shuffle",command=self.shuffle).pack()

        window.mainloop()#create an event loop
    #choose four random cards
    def shuffle(self):
        random.shuffle(self.imageList)
        for i in range(4):
            self.labelList[i]["image"]=self.imageList[i]

deckcardgui( )

