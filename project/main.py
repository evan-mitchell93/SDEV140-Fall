import tkinter as tk

#create the main window of the application
main_window = tk.Tk()

#set the title of the main window
main_window.title("Our first GUI")


#a button is a type of widget you can add
chalet_img = tk.PhotoImage(file="chalet.png")
chalet_button = tk.Button(main_window,image=chalet_img,)
#pack, grid and place organize widgets before
#placing them in the parent window

stop_button.pack()
#main loop is an infinite loop that waits for 
#an event to occur like key pressed until window
#is closed
main_window.mainloop()