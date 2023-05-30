from tkinter import Toplevel, Button
from creational.factory import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("EQs")
        self.geometry("840x480")
        self.button = Button(self, text='Show Guitars', command=self.show_Guitars)
        self.button.pack(expand=True)



    def show_Guitars(self):
        guitarsFactory = GuitarsFactory()

        guitars = guitarsFactory.guitars

        for e in guitars:
            self.button = Button(self, text=f'{e.name}')
            self.button.pack(expand=True)
