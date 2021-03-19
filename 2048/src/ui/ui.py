
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
from game2048 import Game2048
from score_repository import ScoreRepository

class Userinterface:
    
    def __init__(self):
        self.game = Game2048(4)
        self.rep = ScoreRepository()
