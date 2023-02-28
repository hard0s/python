from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Тестовое приложение")
root.geometry("300x250")
root.iconbitmap(default = "./test_logo.ico")

clicks = 0
def click_button():
    global clicks
    clicks += 1
    for i in range(99):
        clicks += 1

    btn["text"] = f"хромосом {clicks}"



lable = ttk.Label(text = "счетчик хромосом никиты", background="#FF1100", foreground="#FFF00C")
lable.pack()


btn = ttk.Button(text = "Click me", command = click_button)
btn.pack(expand = True)
 
root.mainloop()