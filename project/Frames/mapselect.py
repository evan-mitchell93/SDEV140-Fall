from tkinter import *

from characterselect import CharacterSelect
class MapSelect(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text="Main Page of Application")
        label.pack(padx=10,pady=10)
        self.grid(row=0,column=0)
        self.configure(bg="#000")
        img = PhotoImage(file="..\images\chalet.png")
        panel = Label(self, image=img)
        panel.pack(side="right",fill="both",expand="yes")

        select_button = Button(
            self,
            text="Go to Character Selection",
            command=lambda: controller.show_frame(CharacterSelect)
        )


        select_button.pack(side="bottom")