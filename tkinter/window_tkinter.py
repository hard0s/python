from tkinter import *
from tkinter import ttk
from random import choice
 
clicks = 0
colors = ['white', 'black', 'gray', 'brown', 'red', 'orange', 'yellow', 'lime', 'green', 'cyan', 'blue', 'navy', 'magenta', 'purple', 'violet', 'pink']

 
def click_button():
    global clicks
    clicks += 10**2
    # btn["bg"] = choice(colors)
    btn["text"] = f"хромосом {clicks}"   
    
root = Tk()
root.title("оконное приложение")
root.geometry("500x500")
 
btn = ttk.Button(text="Click Me", command=click_button)
# btn.configure(background = choice(colors), foreingground=choice(colors))
# ttk.Style().configure( bg = choice(colors), foreingground=choice(colors))
btn.pack(pady=150)
 
root.mainloop()