
from score_repository import ScoreRepository
from game2048 import Game2048
import pygame as pg
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)

class Userinterface:
    """Luokka, jonka avulla pelin käyttöliittymä toimii.
    Attrbutes:
            game: uusi peli
            rep: Pisteiden hallinta
    """
    def __init__(self):
        """Luokan konstruktori, joka käynnstää pelin
        """
        self.game = Game2048(4)
        self.rep = ScoreRepository()
