from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Тестовое приложение")
root.geometry("500x500")
clicks = 0
def click():
    global clicks
    clicks += 1
    btn["text"] = f"хромосом {clicks}"
    if clicks >= 10:



btn = ttk.Button(text="тест", command=click, state = DISABLED)
btn.place(x = 30, y = 170)
canvas = Canvas(root, width = 500, height = 500, background="black")
canvas.pack(anchor = CENTER, expand = 1 )
canvas.create_line(10, 20, 100,250, activefill="#88FFCC", fill = "#00FF00")

root.mainloop()