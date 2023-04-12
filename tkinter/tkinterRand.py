from tkinter import *
import random
from random import choice

root = Tk()
root.title = "случайные фигуры"
root.geometry = "1000x1000"

size = 600
canvas =Canvas(root, width = size, height = size)
canvas.pack()
i = 0
while True :
    color = choice(['#00ff00', '#000000', '#ffffff', '#FF00ff', '#00ffff', '#ffff00', '#d00f19', '#131954','#fc3465','#32fd43', '#01212f', '#000000', '#30f150',
                    '#ff0a0a'])
    x0 = random.randint(0, size)
    y0 = random.randint(0, size)
    x1 = random.randint(0, size)
    y2 = x1
    d = random.randint(0, size/5)
    canvas.create_line(x0,y0,x1, y2, fill = color)
    canvas.create_rectangle(x0, y0, x1, y2, fill = color)
    canvas.create_oval(x0, y0, x0+d, y0+d, fill=color) 
    root.update()
    i+=1
