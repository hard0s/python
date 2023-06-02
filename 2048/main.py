# GPL 3.2 License author Egor Gysev. Contributors may not be used to endorse or promote products derived from this software without specific prior written permission.
from tkinter import *
from creational.Board import Board
from creational.Game import Game

board = Board()
root = Game( board )
root.start()