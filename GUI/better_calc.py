from breezypythongui import EasyFrame

class Calc(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Calc",width=500,height=500)
        self.setBackground("#E6E6FA")
        self.expression = ""
    
        self.entry_box = self.addTextField(text=" ",row=0,column=0,columnspan=4,sticky="NSEW")
        self.addButton(text="0",row=1,column=0,sticky="NSEW",command=lambda: self.press(0))
        self.addButton(text="1",row=1,column=1,sticky="NSEW",command=lambda: self.press(1))
        self.addButton(text="2",row=1,column=2,sticky="NSEW",command=lambda: self.press(2))
        self.addButton(text="3",row=2,column=0,sticky="NSEW",command=lambda: self.press(3))
        self.addButton(text="4",row=2,column=1,sticky="NSEW",command=lambda: self.press(4))
        self.addButton(text="5",row=2,column=2,sticky="NSEW",command=lambda: self.press(5))
        self.addButton(text="6",row=3,column=0,sticky="NSEW",command=lambda: self.press(6))
        self.addButton(text="7",row=3,column=1,sticky="NSEW",command=lambda: self.press(7))
        self.addButton(text="8",row=3,column=2,sticky="NSEW",command=lambda: self.press(8))
        self.addButton(text="9",row=4,column=1,sticky="NSEW",command=lambda: self.press(9))
        self.addButton(text="+",row=1,column=3,sticky="NSEW",command=lambda: self.press("+"))
        self.addButton(text="-",row=2,column=3,sticky="NSEW",command=lambda: self.press("-"))
        self.addButton(text="*",row=3,column=3,sticky="NSEW",command=lambda: self.press("*"))
        self.addButton(text="=",row=4,column=3,sticky="NSEW",command=lambda: self.equal_press())


    def press(self,num):
        self.expression = self.expression + str(num)
        self.entry_box.setText(self.expression)
    
    def equal_press(self):
        total = str(eval(self.expression))
        self.entry_box.setText(total)
        self.expression = ""

Calc().mainloop()