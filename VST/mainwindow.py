from tkinter import *
from creational.single import Singleton
import eqswin
import guitwin
import footer

class Window(Tk, Singleton): # Наследуем класс ТК и Singleton
    def init(self):
        print ("Calling from init")
        super().__init__()

        self.button = Button(self, text="Open EQs", command=self.create_window_eqs)
        self.button.pack(expand=True)
        self.button = Button(self, text="Open Guitars", command=self.create_window_guitars)
        self.button.pack(expand=True)
        self.button = Button(self, text="Open Footer", command=self.create_footer_eqs)
        self.button.pack(expand=True)



    def create_window_eqs(self):
        global extraWindow
        extraWindow = eqswin.Extra()

    def create_window_guitars(self):
        global extraWindow
        extraWindow = guitwin.Extra()

    def create_footer_eqs(self):
        global extraWindow
        extraWindow = footer.Extra()

    def __init__(self):
        print('calling from __init__')