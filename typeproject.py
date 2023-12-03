from breezy import EasyFrame
import time
from tkinter import *

start = None
stop = None

class Typer(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,width=500,height=500)
        self.config(bg="pink")
        self.FLAG = False
        self.list_of_words = ["Hello","Goodbye","Avery","Project","Pokemon","SDEV"]
        self.word_counter = 0
        self.word_first = self.addTextField(text=self.list_of_words[0],row=0,column=0)
        self.word_box = self.addTextField(text="",row=1,column=0)
        self.word_box.focus()
        self.word_box.bind("<KeyRelease>",self.pressed)

    def pressed(self,keyevent):
        word = self.word_first.get()
        word_size = len(word)
        repeat_word = self.word_box.get()
        repeat_word_size = len(repeat_word)
        if self.FLAG == False:
            global start
            start = time.time()
            print("Timer started")
            self.FLAG = True

        if word_size == repeat_word_size and repeat_word == word:
            stop = time.time()
            totaltime = stop - start
            print(f"Total time: {totaltime:.2f}")
            if self.word_counter < len(self.list_of_words) -1:
                self.word_first.setValue(self.list_of_words[self.word_counter + 1])
                self.word_box.setValue("")
                self.word_counter += 1
                self.FLAG = False

    
Typer().mainloop()
