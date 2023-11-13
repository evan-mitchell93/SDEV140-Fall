"""
Evan Mitchell
SDEV 140 Project Examples
11/9/2023

"""

from tkinter import *
from tkinter import messagebox
from mapselect import MapSelect
from characterselect import CharacterSelect

class Window(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)

        #setup main window configurations
        self.title("R6 Seige Operator Tips")
        self.configure(bg='#E6E6FA')

        #create frames to switch between
        self.frames = {"character_frame":CharacterSelect(self),"map_frame":MapSelect(self)}
        self.show_frame("map_frame")

    #function to hide all frames that are not selected and show the selected one
    def show_frame(self,name):
        for f in self.frames:
            if f == name:
                self.frames[name].tkraise()
                self.frames[name].grid(row=0,column=0)
            else:
                if self.frames[f].winfo_manager():
                    self.frames[f].grid_forget()


if __name__ == "__main__":
    win = Window()
    win.minsize(600,400)
    win.mainloop()