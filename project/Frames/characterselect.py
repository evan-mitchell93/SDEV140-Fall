from tkinter import *
class CharacterSelect(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text="Character Selection")
        label.pack(padx=10,pady=10)
        self.grid(row=0,column=0)
