from tkinter import *
from PIL import Image,ImageTk
class CharacterSelect(Frame):
    def __init__(self,parent):
        self.map = ""
        Frame.__init__(self,parent)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid(row=0,column=0)
        self.configure(bg="#ffe1f5")
        operators = [["ace","amaru","ash","blackbeard","blitz"],["brava","buck","capitao","dokkaebi","finka"],
                     ["flores","fuze","glaz","gridlock","grim"],["hibana","iana","iq","jackal","kali"],["lion","maverick","montagne","nomad","nokk"],
                     ["osa","ram","sens","sledge","thatcher"],["thermite","twitch","ying","zero","zofia"]]

        for row_index,row in enumerate(operators):
            for column_index, column in enumerate(row):
                name = column
                temp = Image.open(f"../images/operators/{name}.png")
                temp = temp.resize((50,50), Image.ADAPTIVE)
                op_img = ImageTk.PhotoImage(temp)
                op_label = Label(self,image = op_img,width=50,height=50)
                op_label.grid(row=row_index,column=column_index + 1,padx=2,pady=2)
                op_label.image = op_img

