from breezypythongui import EasyFrame

class Match(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Match",width=500,height=500)
        self.config(bg="green")
        self.round_w = 0
        self.round_l = 0

        self.addButton(text="Round Won",row=2,column=0,command=self.round_won)
        self.addButton(text="Round Lost",row=2,column=1,command=self.round_lost)

    
    def round_won(self):
        self.round_w += 1
        if self.round_w == 4 and self.round_l < 3:
            print("You won the match")
            self.destroy()
        
    def round_lost(self):
        self.round_l += 1
        if self.round_l == 4 and self.round_w < 3:
            print("You lost the match")
            self.destroy()