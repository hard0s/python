# from tkinter import *
import random
from random import choice


# diaposon = 0

# root = Tk()
# root.title = "случайные фигуры"
# root.geometry = "1000x1000"

# size = 600
# canvas =Canvas(root, width = size, height = size)
# canvas.pack()
# i = 0
# while i < 1000 :
#     color = choice(['#00ff00', '#000000', '#ffffff', '#FF00ff', '#00ffff', '#ffff00', '#d00f19', '#131954','#fc3465','#32fd43'])
#     x0 = random.randint(0, size)
#     y0 = random.randint(0, size)
#     x1 = random.randint(0, size)
#     y2 = x1
#     d = random.randint(0, size/5)
#     canvas.create_arc(x0, y0, x1, y2, fill = color)
#     canvas.create_line(x0,y0,x1, y2, fill = color)
#     canvas.create_rectangle(x0, y0, x1, y2, fill = color)
#     canvas.create_oval(x0, y0, x0+d, y0+d, fill=color) 
#     root.update()
#     i+=1
from math import *
from tkinter import *

f = input('f(x):')

root = Tk()

canv = Canvas(root, width = 1000, height = 1000, bg = "white")
canv.create_line(500,1000,500,0,width=2,arrow=LAST) 
canv.create_line(0,500,1000,500,width=2,arrow=LAST) 

First_x = -500;

for i in range(16000):
	color = choice(['#00ff00', '#000000', '#ffffff', '#FF00ff', '#00ffff', '#ffff00', '#d00f19', '#131954','#fc3465','#32fd43'])
	x = First_x + (1 / 16) * i
	new_f = f.replace('x', str(x))
	y = -eval(new_f) + 500
	x += 500
	canv.create_oval(x, y, x + 1, y + 1,width=f, fill = color)
	 
canv.pack()	
root.mainloop()





