from tkinter import *


win = Tk()
i = 0
while i <= 9:
    frame = Frame(win)
    frame.grid()
    button= Button(frame,text=f"button {i}")
    button.pack()


win.title("Buttons")

win.mainloop()