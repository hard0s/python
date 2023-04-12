from tkinter import Tk, Canvas
import random

def main():
    size = 480
    root = Tk()
    canvas = Canvas(root, width=size, height=size)
    canvas.pack()
    
    while True:
        hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        x = random.randint(0, size)
        y = random.randint(0, size)
        d = random.randint(0, size/5)
        canvas.create_oval(x, y, x+d, y+d, outline="#000000",fill=hexadecimal, width=2)
        root.update()
        hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        x = random.randint(0, size)
        y = random.randint(0, size)
        d = random.randint(0, size/5)
        canvas.create_rectangle(x, y, x+d, y+d, outline="#000000",fill=hexadecimal, width=2)
        root.update()

if __name__ == '__main__':
    main()