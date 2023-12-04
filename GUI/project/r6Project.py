from breezypythongui import EasyFrame
import tkinter as tk
from main_frame import MainFrame
from match_frame import Match


#Base Application Window
root = tk.Tk()

###Create an object from class MainFrame
main_window = MainFrame()
main_window.grid(row=0,column=0)

match_window = None

def start_match():
    global match_window
    match_window = Match()
    match_window.grid(row=0,column=0,sticky="NSEW")
    finish_btn = tk.Button(match_window,text="Finish Match", command=finish_match)
    finish_btn.grid(row=0,column=0)

def finish_match():
    match_window.grid_forget()

#Associate the start_btn with the main windows
start_btn = tk.Button(main_window,text="Start Match",command=start_match)
start_btn.grid(row=0,column=0)

root.mainloop()