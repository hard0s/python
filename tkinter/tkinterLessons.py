import tkinter 
import math
import random
from random import choice
from tkinter import ttk
tk = tkinter.Tk()
colors = ['white', 'black', 'gray', 'brown', 'red', 'orange', 'yellow', 'lime', 'green', 'cyan', 'blue', 'navy', 'magenta', 'purple', 'violet', 'pink']
def random_color():
    lb['bg'] = choice(colors) 
    # lb['fg'] = choice(colors) 


lb = tkinter.Lable(text = "нигга", background = random_color() )
lb.pack()

tk.mainloop()