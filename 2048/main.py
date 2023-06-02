from tkinter import *
from creational.Game import Game
from creational.Board import Board

gamepanel =Board()
game2048 = Game( gamepanel)
game2048.start()