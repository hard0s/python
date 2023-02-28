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
    btn["text"] = f"Никита гей {clicks}"

            


btn = ttk.Button(text = "Click me", command = click_button)
btn.pack(padx = 20, pady = 50)
 
root.mainloop()