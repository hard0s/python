
from tkinter import *
from random import choice



root = Tk()
root.geometry = ('500x500')

colors = ['white', 'black', 'gray', 'brown', 'red', 'orange', 'yellow', 'lime', 'green', 'cyan', 'blue', 'navy', 'magenta', 'purple', 'violet', 'pink']


def random_color():
    button['bg'] = choice(colors) 
    button['fg'] = choice(colors) 



button = Button(root, text='Нажми меня и я поменяю цвет', command=random_color)
button.pack()

root.mainloop()