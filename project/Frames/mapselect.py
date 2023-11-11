from tkinter import *

from characterselect import CharacterSelect
map_list = ["Border","Chalet","Clubhouse","Bank",
            "Kafe","Oregon","Skyscraper","Theme Park",
            "Villa","Outback","Coastline","Consulate",
            "Consulate","Emerald Plains","Stadium Bravo","Nighthaven Labs"]

class MapSelect(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.root = parent
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid(row=0,column=0)
        self.configure(bg="#ffa1fe")

        self.selected = StringVar(value="Border")
        menu = OptionMenu(self,self.selected, *map_list)
        menu.grid(row=0,column=0)

        map_button = Button(self,command=self.pick_map,text="Select",cursor="plus")
        map_button.grid(row=1,column=0)
    #Once map is selected, create a Character Select Frame with that map argument

    def pick_map(self):
        print("Map chosen")
        self.root.frames["character_frame"].map = self.selected
        self.root.show_frame("character_frame")
