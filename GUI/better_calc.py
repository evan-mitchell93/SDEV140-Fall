from breezypythongui import EasyFrame

class Calc(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Calculator",width=500,height=500)
        self.setBackground("#E6E6FA")
        self.expression = ""

        self.entry_box = self.addTextField(text="",row=0,column=0,columnspan=5,sticky="NSEW")
        #first row of buttons
        self.addButton(text="0",row=1,column=0,sticky="NSEW",command=lambda:self.press(0))
        self.addButton(text="1",row=1,column=1,sticky="NSEW",command=lambda: self.press(1))
        self.addButton(text="2",row=1,column=2,sticky="NSEW",command=lambda: self.press(2))
        #second row of buttons
        self.addButton(text="3",row=2,column=0,sticky="NSEW",command=lambda: self.press(3))
        self.addButton(text="4",row=2,column=1,sticky="NSEW",command=lambda: self.press(4))
        self.addButton(text="5",row=2,column=2,sticky="NSEW",command=lambda: self.press(5))
        #Third and 4th row of buttons
        self.addButton(text="6",row=3,column=0,sticky="NSEW",command=lambda: self.press(6))
        self.addButton(text="7",row=3,column=1,sticky="NSEW",command=lambda: self.press(7))
        self.addButton(text="8",row=3,column=2,sticky="NSEW",command=lambda: self.press(8))
        self.addButton(text="9",row=4,column=1,sticky="NSEW",command=lambda: self.press(9))

        #weird place just for Avery
        self.addButton(text="C",row=4,column=0,sticky="NSEW",command= self.clear_all)
        #op buttons
        self.addButton(text="+",row=1,column=4,sticky="NSEW",command=lambda:self.press("+")).config(bg="#D8FFB1")
        self.addButton(text="-",row=2,column=4,sticky="NSEW",command=lambda:self.press("-")).config(bg="#D8FFB1")
        self.addButton(text="*",row=3,column=4,sticky="NSEW",command=lambda:self.press("*")).config(bg="#D8FFB1")

        #equals button
        self.eb = self.addButton(text="=",row=4,column=2,columnspan=3,sticky="NSEW",command=self.evaluate)
        self.eb["state"] = "disabled"
    def evaluate(self):
        total = str(eval(self.expression))
        self.entry_box.setText(total)
        self.expression = ""

    def press(self,num):
        self.expression = self.expression + str(num)
        self.entry_box.setText(self.expression)

    def clear_all(self):
        self.expression = ""
        self.entry_box.setText(self.expression)

def main():
    Calc().mainloop()

if __name__ == "__main__":
    main()