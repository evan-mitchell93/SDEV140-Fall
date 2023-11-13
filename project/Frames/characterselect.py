from tkinter import *
from PIL import Image,ImageTk
class CharacterSelect(Frame):
    def __init__(self,parent):
        self.map = ""
        self.root = parent
        Frame.__init__(self,parent)
        self.grid(row=0,column=0)
        self.configure(bg="#ffe1f5")
        attack_ops = [["ace","amaru","ash","blackbeard","blitz"],["brava","buck","capitao","dokkaebi","finka"],
                     ["flores","fuze","glaz","gridlock","grim"],["hibana","iana","iq","jackal","kali"],["lion","maverick","montagne","nomad","nokk"],
                     ["osa","ram","sens","sledge","thatcher"],["thermite","twitch","ying","zero","zofia"]]
        
        defend_ops = []
        op_text = Label(self,text="Choose an operator")
        op_text.grid(row=0,column=0,columnspan=2)
        check1 = IntVar()
        check2 = IntVar()
        attack_check = Checkbutton(self,text="Attackers",variable=check1, command=self.show_ops(attack_ops))
        defense_check = Checkbutton(self,text="Defenders",variable=check2,command=self.show_ops(defend_ops))
        attack_check.grid(row=1,column=0)
        defense_check.grid(row=1,column=1)

        back_button = Button(text="Back", command=self.go_back)
        back_button.grid()

    def go_back(self):
        self.root.show_frame("map_frame")
        
    def show_ops(self,op_set):
        for row_index,row in enumerate(op_set):
            for column_index, column in enumerate(row):
                name = column
                temp = Image.open(f"../images/operators/{name}.png")
                temp = temp.resize((50,50), Image.ADAPTIVE)
                op_img = ImageTk.PhotoImage(temp)
                op_label = Label(self,image = op_img,width=50,height=50)
                op_label.grid(row=row_index + 3,column=column_index,padx=2,pady=2)
                op_label.image = op_img