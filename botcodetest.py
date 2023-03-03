from tkinter import *
# создать окно
root = Tk()
# добавить лейбл для вопроса
question = Label(root, text="Какой язык программирования используется для создания веб-сайтов?")
question.pack()
# добавить поле для ввода ответа
answer = Entry(root)
answer.pack()
# добавить кнопку для проверки правильности ответа
check = Button(root, text="Проверить")
check.pack()
# функция для проверки правильности ответа
def checkAnswer():
    if answer.get() == "HTML":
        print("Верный ответ!")
    else:
        print("Неверный ответ!")
# связать кнопку с функцией
check.configure(command=checkAnswer)
# запустить приложение
root.mainloop()