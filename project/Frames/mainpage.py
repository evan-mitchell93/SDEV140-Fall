from tkinter import *
from mapselect import MapSelect
class MainPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text="Main Page of Application")
        label.pack(padx=10,pady=10)
        self.grid(row=0,column=0)

        switch_button = Button(
            self,
            text="Go to Map Selection",
            command=lambda: controller.show_frame(MapSelect)
        )
        switch_button.pack(side="bottom")