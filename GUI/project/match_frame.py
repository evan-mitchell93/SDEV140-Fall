from breezypythongui import EasyFrame
import tkinter
from mods.match import GameMatch
from mods.ops import Operator
import pickle
from PIL import ImageTk,Image

class Match(EasyFrame):

    rounds_played = 0
    def __init__(self):
        EasyFrame.__init__(self,title="Match",width=500,height=500)
        self.config(bg="#869eb9")
        self.match = GameMatch("emitchell")
        self.all_ops = {"tachanka":"defend","castle":"defend","nomad":"attack","sens":"attack","valkyrie":"defend","thatcher":"attack"}
        self.op_name = self.prompterBox(title="Operator",promptString="Pick an operator",inputText="",fieldWidth=20)
        self.current_op = ""
        try:
            fp = open(f"{self.op_name}.obj","rb")
            self.current_op = pickle.load(fp)
        except:
            self.update_operator()
        
        self.round_lable = self.addTextField(text=f"{self.match.wins} : {self.match.loses}",row=0,column=0,columnspan=2,sticky="NSEW")
        self.addButton(text="Round Won",row=1,column=0,command=self.round_won,sticky="NSEW").config(bg="#64ad6a")
        self.addButton(text="Round Lost",row=1,column=1,command=self.round_lost,sticky="NSEW").config(bg="#dd3439")
        self.display = self.addTextField(text=f"{self.current_op.name}, Wins: {self.current_op.wins}, Loses: {self.current_op.loses}",row=2,column=0,sticky="NSEW")

        self.save_btn = self.addButton(text="save",row=3,column=0,command=self.save_match,sticky="NSEW").config(bg="#7cb9e8")
        self.load_btn = self.addButton(text="load",row=3,column=1,command=self.load_match,sticky="NSEW").config(bg="#3b43d6")

    def update_operator(self):
       fp = open(f"{self.op_name}.obj","wb")
       pickle.dump(self.current_op,fp)
       fp.close()
       self.op_name = self.prompterBox(title="Operator",promptString="Pick an operator",inputText="",fieldWidth=20)
       self.img = ImageTk.PhotoImage(Image.open(f"./r6/{self.op_name}.png").resize((150,150)))
       self.img_label = self.addLabel(text="",row=2,column=1,sticky="NSEW")
       self.img_label.configure(image=self.img)
       self.image = self.img

       try:
        fp = open(f"{self.op_name}.obj","rb")
        self.current_op = pickle.load(fp)
        fp.close()

       except:
        self.current_op = Operator(self.op_name,self.all_ops[self.op_name])

    def update_display(self):
       self.display.setText(f"{self.current_op.name}, Wins: {self.current_op.wins}, Loses: {self.current_op.loses}")

    def save_match(self):
        fp = open("frames.obj",'wb')
        pickle.dump(self.match,fp)
        fp.close()
        self.destroy()
    
    def load_match(self):
        fp = open("frames.obj","rb")
        self.match = pickle.load(fp)
        fp.close()
        self.round_lable.setText(f"{self.match.wins} : {self.match.loses}")
        self.update_operator()
        self.update_display()

    def round_won(self):
        self.match.wins += 1
        self.current_op.wins += 1
        self.round_lable.setText(f"{self.match.wins} : {self.match.loses}")
        self.update_display()
        if self.match.wins == 4 and self.match.loses < 3:
            print("You won the match")
            self.destroy()
        self.update_operator()


        
    def round_lost(self):
        self.match.loses += 1
        self.current_op.loses += 1
        self.round_lable.setText(f"{self.match.wins} : {self.match.loses}")
        self.update_display()
        if self.match.loses == 4 and self.match.wins < 3:
            print("You lost the match")
            self.destroy
        self.update_operator()