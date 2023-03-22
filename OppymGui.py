# -*- coding utf-8 -*-
from tkinter import *
import math


tk = Tk()
tk.title('Test gui')
#
button = Button()
button["text"]="Quit"
button["command"]=tk.quit
button.pack()
#
canvas = Canvas()
canvas["height"] = 480
canvas["width"] = 800
canvas["background"] = "#eeeeff"
canvas["borderwidth"] = 2
canvas.pack()
#
canvas.create_text[20, 10, "text=20, 10"]
canvas.create_text[480, 800, "text=480, 600"]
tk.mainloop()