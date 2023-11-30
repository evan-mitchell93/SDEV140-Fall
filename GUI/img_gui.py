from breezypythongui import EasyFrame
from tkinter import PhotoImage

class IMGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Images",width=500,height=500)
        self.config(bg=("blue"))

        #list of ops
        self.ops = ['ace','alibi','amaru']
        counter = 0


        for name in self.ops:
            #make a photoimage
            img = PhotoImage(file=f'./r6/{name}.png')
            #make a label to house the image
            lbl = self.addLabel(text="",row=0,column=counter)
            lbl.config(image=img)
            lbl.image = img
            counter += 1
IMGUI().mainloop()