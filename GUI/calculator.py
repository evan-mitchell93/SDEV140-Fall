from breezypythongui import EasyFrame

class CalculatorGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Calculator App")
        #input label and IntegerFields
        self.addLabel(text="First Operand",row=0,column=0)
        self.first_op = self.addIntegerField(value=0,row=1,column=0)
        self.addLabel(text="Second Operand",row=0,column=2)
        self.second_op = self.addIntegerField(value=0,row=1,column=2)

        #Operations buttons 
        self.addButton(text = "+",row=3,column=0,command=self.add_ops)
        self.addButton(text = "-",row=3,column = 1, command=self.sub_ops)
        self.addButton(text = "*",row=3,column = 2, command=self.multi_ops)
        self.addButton(text = "/",row=3,column = 3, command=self.div_ops)
        self.addButton(text = "%",row=3,column = 4, command=self.mod_ops)
        self.addLabel(text="Result",row=5,column=5)
        self.res = self.addIntegerField(value=0,row=6,column=6)
        
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
