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
        self.title("R6 Seige Operator Tips")
        self.configure(bg='#E6E6FA')
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.frames = {"character_frame":CharacterSelect(self),"map_frame":MapSelect(self)}
        self.frames["character_frame"].grid(row=0,column=0)
        self.frames["character_frame"].grid_forget()
        self.frames["map_frame"].grid(row=0,column=0)


    def show_frame(self,name):
        for frame in self.frames:
            if frame == name:
                self.frames[frame].grid(row=0,column=0)
                self.frames[frame].tkraise()
            else:
                self.frames[frame].grid_forget()

if __name__ == "__main__":
    win = Window()
    win.minsize(600,400)
    win.mainloop()