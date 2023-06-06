import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

# функция для построения графика
def plot_func():
    # получаем начальное и конечное значения диапазона по оси X
    x_min = float(x_min_entry.get())
    x_max = float(x_max_entry.get())
    # создаем массив значений X в заданном диапазоне
    x = np.linspace(x_min, x_max, num=1000)
    # вычисляем значения функции для всех значений X
    y = eval(function_entry.get())
    # очищаем ранее нарисованный график
    plt.clf()
    # настраиваем график
    plt.plot(x, y, color=color_entry.get(), linewidth=float(linewidth_entry.get()))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of ' + function_entry.get())
    # выводим график на экран
    plt.show()
# создаем окно приложения
root = Tk()
root.title("Function plotter")
# создаем элементы управления: поля ввода и метки
function_label = Label(root, text="Function:")
function_label.grid(row=0, column=0)
function_entry = Entry(root, width=30)
function_entry.grid(row=0, column=1)
color_label = Label(root, text="Color:")
color_label.grid(row=1, column=0)
color_entry = Entry(root, width=10)
color_entry.grid(row=1, column=1)
color_entry.insert(END, "blue")
linewidth_label = Label(root, text="Line width:")
linewidth_label.grid(row=2, column=0)
linewidth_entry = Entry(root, width=10)
linewidth_entry.grid(row=2, column=1)
linewidth_entry.insert(END, "1.0")
x_min_label = Label(root, text="X min:")
x_min_label.grid(row=3, column=0)
x_min_entry = Entry(root, width=10)
x_min_entry.grid(row=3, column=1)
x_min_entry.insert(END, "-10.0")
x_max_label = Label(root, text="X max:")
x_max_label.grid(row=4, column=0)
x_max_entry = Entry(root, width=10)
x_max_entry.grid(row=4, column=1)
x_max_entry.insert(END, "10.0")
plot_button = Button(root, text="Plot function", command=plot_func)
plot_button.grid(row=5, column=1)
# запускаем главный цикл обработки событий
root.mainloop()