from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Тестовое приложение")
root.geometry("300x250")
root.iconbitmap(default = "./test_logo.ico")
def test_click(event):
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()
            easy()
def easy():
       btna1 = ttk.Button(text = "начать тест", command = start)
       btna1.pack(expand = True)
       


def start():
       btna1 = ttk.Button(text = "начать тест")
       btna1.destroy()
       python = "python"
       lang = StringVar(value = python)
       python_btn = ttk.Radiobutton(text="python", value=python, variable=lang)
       python_btn.pack()
       java = "java"
       java_btn = ttk.Radiobutton(text="java", value=java, variable= java)
       java_btn.pack()

       
def click_button():
    global clicks
    clicks += 1
    if clicks == 1:
        btn.destroy()

        #btn1.bind('<ButtonPress-1>', test_click())

        btn1.pack(anchor="n", pady = 20 )
        btn2.pack(anchor="center")
        btn3.pack(anchor="s", pady = 20)

clicks = 0
btn1 = ttk.Button(text = "Легкая сложность")
btn1.bind('<ButtonPress-1>',test_click)
btn2 = ttk.Button(text = "Нормальная сложность")
btn3 = ttk.Button(text = "Трудная сложность")

        



lable = ttk.Label(text = "Начать тест", background="#000000", foreground="white")
lable.pack()


btn = ttk.Button(text = "Начать", command = click_button)
btn.pack(expand = True)
root.mainloop()