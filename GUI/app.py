from breezypythongui import EasyFrame

class Demo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Demo app")

        self.addLabel(text="First Name",row=0,column=0)
        self.f_name = self.addTextField(text="",row=1,column=0)
        self.addButton(text = "Echo",row=3,column=0,columnspan=2,command = self.echo_name)

    def echo_name(self):
        print(self.f_name.getValue())
        self.f_name.setValue("")
Demo().mainloop()
