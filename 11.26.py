from tkinter import *
def pressis():
    wht =Tk( )
    label=Label(wht,text="WHTDSB")
    label.pack()
    wht.mainloop()

wht =Tk( )
label=Label(wht,text="WHT")
button1=Button(wht,text="is sb",fg="red",command=pressis)
button2=Button(wht,text="isn't sb")
label.pack()
button1.pack()
button2.pack()


wht.mainloop()
