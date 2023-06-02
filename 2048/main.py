from tkinter import *
from creational.Board import Board
from creational.Game import Game

gamepanel =Board()
game2048 = Game( gamepanel)
game2048.start()