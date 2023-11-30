from breezypythongui import EasyFrame

class MainFrame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Game",height=500,width=500)
        self.config(bg="blue")

