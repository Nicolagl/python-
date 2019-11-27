from tkinter import *
import tkinter.messagebox
from chess import isvalid
class sudokuGUI:
    def __init__(self):
        win=Tk()
        win.title("check sudoku solution")
      
        frame=Frame(win)
        frame.pack()

        self.cells=[]
        for i in range(9):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(StringVar())
        for i in range(9):
            for j in range(9):
                Entry(frame,width=5, justify=RIGHT,textvariable=self.cells[i][j]).grid(row=i,column=j)
        Button(win,text="Validate",command=self.validate).pack()
        win.mainloop()
    def validate(self):
        values=[[eval(x.get())
                 for x in self.cells[i]] for i in range(9)]
        if isvalid(values):
            tkinter.messagebox.showinfo("Check sudoku solution","is valid")
        else:
             tkinter.messagebox.showinfo("Check sudoku solution","Failed")
sudokuGUI()
