from breezypythongui import EasyFrame
from match import GameMatch
import pickle
class Match(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Match",width=500,height=500)
        self.config(bg="green")
        self.match = GameMatch("emitchell")
        self.addButton(text="Round Won",row=1,column=0,command=self.round_won)
        self.addButton(text="Round Lost",row=1,column=1,command=self.round_lost)
        self.addButton(text="save",row=2,column=0,command=self.save_match)
        self.addButton(text="load",row=2,column=1,command=self.load_match)

    def save_match(self):
        return
    def round_won(self):
        self.match.wins += 1
        print(self.match.wins)
        if self.match.wins == 4 and self.match.loses < 3:
            print("You won the match")
            self.destroy()
        
    def round_lost(self):
        self.match.loses += 1
        print(self.match.loses)
        if self.match.loses == 4 and self.match.wins < 3:
            print("You lost the match")
            self.destroy()