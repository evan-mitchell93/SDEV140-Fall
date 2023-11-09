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
        self.title("Our GUI application")
        #root.configure(bg='#E6E6FA')

        #setup a Frame 
        container = Frame(self,height=400,width=600, bg='#E6E6FA')
        container.pack(side="top", fill="both",expand=True)
        container.grid_columnconfigure(0,weight=1)
        container.grid_rowconfigure(0,weight=1)
        #add our other pages to a dictionary
        self.frames = {}
        for F in (MainPage,MapSelect,CharacterSelect):
            frame = F(container,self)
            frame.configure(height=400,width=600)
            self.frames[F] = frame

        #call show frame for the first page on launch
        self.show_frame(MainPage)

    def show_frame(self,name):
        frame = self.frames[name]
        frame.tkraise()

if __name__ == "__main__":
    win = Window()
    win.mainloop()