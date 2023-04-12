from math import *
from tkinter import *

def main():
    f = input('f(x):')
    color = input('color:')
    root = Tk()
    canvas = Canvas(root, width=400, height=400)
    canvas.create_line(200,400,200,0,width=1,arrow=LAST) 
    canvas.create_line(0,200,400,200,width=1,arrow=LAST) 
    
    First_x = -200

    for i in range(16000):
        if (i % 400 == 0):
            k = First_x + (1 / 16) * i
            canvas.create_line(k + 200, -3 + 200, k + 200, 3 + 200, width = 0.5, fill = 'black')
            if (k != 0):
                canvas.create_line(-3 + 200, k + 200, 3 + 200, k + 200, width = 0.5, fill = 'black')
        try:
            x = First_x + (1 / 16) * i
            new_f = f.replace('x', str(x))
            y = -eval(new_f) + 200
            x += 200
            canvas.create_oval(x, y, x + 1, y + 1, fill = 'black')
        except:
            pass

    canvas.pack()
    root.mainloop()
    
    

if __name__ == '__main__':
    main()