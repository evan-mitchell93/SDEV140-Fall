from breezypythongui import EasyFrame
from match import GameMatch
import pickle
class Match(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Match",width=500,height=500)
        self.config(bg="#869eb9")
        self.match = GameMatch("emitchell")
        self.round_lable = self.addTextField(text=f"{self.match.wins} : {self.match.loses}",row=0,column=0,columnspan=2,sticky="NSEW")
        self.addButton(text="Round Won",row=1,column=0,command=self.round_won,sticky="NSEW").config(bg="#64ad6a")
        self.addButton(text="Round Lost",row=1,column=1,command=self.round_lost,sticky="NSEW").config(bg="#dd3439")
        self.save_btn = self.addButton(text="save",row=2,column=0,command=self.save_match,sticky="NSEW").config(bg="#7cb9e8")
        self.load_btn = self.addButton(text="load",row=2,column=1,command=self.load_match,sticky="NSEW").config(bg="#3b43d6")

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


    def round_won(self):
        self.match.wins += 1
        self.round_lable.setText(f"{self.match.wins} : {self.match.loses}")
        print(self.match.wins)
        if self.match.wins == 4 and self.match.loses < 3:
            print("You won the match")
            self.destroy()
        
    def round_lost(self):
        self.match.loses += 1
        self.round_lable.setText(f"{self.match.wins} : {self.match.loses}")
        print(self.match.loses)
        if self.match.loses == 4 and self.match.wins < 3:
            print("You lost the match")
            self.destroy()