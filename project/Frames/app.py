"""
Evan Mitchell
SDEV 140 Project Examples
11/9/2023

"""

from tkinter import *
from tkinter import messagebox
from mainpage import MainPage
from mapselect import MapSelect
from characterselect import CharacterSelect

class Window(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        self.title("R6 Seige Operator Tips")
        self.configure(bg='#E6E6FA')
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)


        #call show frame for the first page on launch
        frame_main = MainPage(self)
        self.show_frame(frame_main)

    def show_frame(self,name):
        frame = name
        frame.tkraise()

if __name__ == "__main__":
    win = Window()
    win.minsize(600,400)
    win.mainloop()