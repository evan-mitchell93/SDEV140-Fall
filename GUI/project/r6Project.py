from breezypythongui import EasyFrame
from tkinter import PhotoImage
import tkinter as tk
from main_frame import MainFrame
from match_frame import Match


root = tk.Tk()

main_window = MainFrame()
main_window.grid(row=0,column=0)

match_window = None

def start_match():
    global match_window
    match_window = Match()
    match_window.grid(row=0,column=0,sticky="NSEW")
    finish_btn = tk.Button(match_window,text="Finish Match", command=finish_match)
    finish_btn.grid(row=1,column=0)

def finish_match():
    match_window.grid_forget()
    main_window.grid(row=0,column=0,sticky="NSEW")

start_btn = tk.Button(main_window,text="Start Match",command=start_match)

start_btn.grid(row=0,column=0)

root.mainloop()