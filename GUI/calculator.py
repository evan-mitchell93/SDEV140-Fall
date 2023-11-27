'''
    Evan Mitchell
    SDEV 140
    tkinter/breezy example - UGLY CALCULATOR
    11/27/2023
'''


from breezypythongui import EasyFrame

class CalculatorGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Calculator App",width=750,height=350)
        self.setBackground("blue")
        #input label and IntegerFields
        self.addLabel(text="First Operand",row=0,column=0,columnspan= 2, sticky="NSEW")
        self.first_op = self.addIntegerField(value=0,row=1,column=0,columnspan= 2, sticky="NSEW")
        self.addLabel(text="Second Operand",row=0,column=2,columnspan=2, sticky="NSEW")
        self.second_op = self.addIntegerField(value=0,row=1,column=2,columnspan=2,sticky="NSEW")

        #Operations buttons
        #STICKY DOESNT WORK BY DEFAULT WITH BREEZY ADD BUTTON - MUST EDIT MODULE FILE
        self.addButton(text = "+",row=3,column = 0,command=self.add_ops,sticky="NSEW")
        self.addButton(text = "-",row=3,column = 1, command=self.sub_ops,sticky="NSEW")
        self.addButton(text = "*",row=3,column = 2, command=self.multi_ops,sticky="NSEW")
        self.addButton(text = "/",row=3,column = 3, command=self.div_ops,sticky="NSEW")
        self.addButton(text = "%",row=3,column = 4, command=self.mod_ops,sticky="NSEW")
        self.addLabel(text="Result",row=4,column=0,columnspan=2,sticky="NSEW")
        self.res = self.addIntegerField(value=0,row=4,column=2,columnspan=2,sticky="NSEW")
        self.addButton(text="C",row=5,column=0,command=self.clear_all,sticky="NSEW")
    
    def clear_all(self):
        self.first_op.setNumber(0)
        self.second_op.setNumber(0)
        self.res.setNumber(0)
        
    def add_ops(self):
        self.res.setNumber(self.first_op.getNumber() + self.second_op.getNumber())

    def sub_ops(self):
        self.res.setNumber(self.first_op.getNumber() - self.second_op.getNumber())

    def div_ops(self):
        self.res.setNumber(self.first_op.getNumber() / self.second_op.getNumber())

    def multi_ops(self):
        self.res.setNumber(self.first_op.getNumber() * self.second_op.getNumber())

    def mod_ops(self):
        self.res.setNumber(self.first_op.getNumber() % self.second_op.getNumber())

CalculatorGUI().mainloop() 