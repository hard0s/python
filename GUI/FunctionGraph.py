from math import *
from tkinter import *

def main():
    f = input('f(x):')
    color = "black"
    root = Tk()
    canvas = Canvas(root, width=1020, height=510)
    canvas.create_line(5, 250, 1005, 250,width=1,arrow=LAST, fill = color) # X asix
    canvas.create_line(5, 500, 5, 0,width=1,arrow=LAST, fill = color) # Y asix
    First_x = -245
    # for i in range(16000):
    #     if (i % 400 == 0):
    #         k = First_x + (1 / 16) * i
    #         canvas.create_line(k+250, -3+250, k+250, 3+250, width = 0.5, fill = "black") # X asix
    #         if (k != 0):
    #             canvas.create_line(3+250, k+250, -3+250, k+250, width = 0.5, fill = "black") # Y asix
    #     try:
    #         x = First_x + (1 / 16) * i
    #         new_f = f.replace('x', str(x))
    #         y = -eval(new_f) + 250
    #         x += 250
    #         canvas.create_oval(x, y, x, y, fill = "black")
    #     except:
    #        pass
    for i in range(16000):
        x = First_x + (1 / 16) * i
        new_f = f.replace('x', str(x))
        y = -eval(new_f) + 250
        x += 250
        canvas.create_oval(x, y, x + 1, y + 1, fill = 'black')

    canvas.pack()
    root.mainloop()

if __name__ == '__main__':
    main()