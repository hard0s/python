import nigga
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Тестовое приложение")
root.geometry("1920x500")
root.iconbitmap(default = "./test_logo.ico")



def test_click(event):
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()
            lable1 = ttk.Label(text = "На каком языке написан этот тест", background=  "#000000", foreground = "#FFFFFF", font = ("Arial", 12))
            lable1.pack()
            easy()
def easy():
       start()
def check():
       answer = ttk.Entry()
       answer.pack(anchor = "center")
       match answer.get():
              case "1":
                     print("Правильно")
              case "2":
                     print("Неправильно")

           

def start():
       btn_check = ttk.Button(root, text = "Проверить")
       btn_check.pack()

       python_btn = ttk.Label(text="1) python")
       python_btn.pack(anchor="center")


       java_btn = ttk.Label(text="2)java")
       java_btn.pack(anchor = "center", pady = 20)
       
       check()
       

       
def click_button():
    global clicks
    clicks += 1
    if clicks == 1:
        btn.destroy()
        lable.destroy()
        

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