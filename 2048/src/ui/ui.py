
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

    def run():
        pass

    def run_test(self):
        print(self.rep.get_top5())
        pelaajat = [("Mixu", 123), ("Pelaaja2", 12), ("ASDSADSAd", 1233451), ("Testi1", 1233)]
        for pelaaja in pelaajat:
            print(self.rep.add_new_highscore(pelaaja[0], pelaaja[1]))
        print(self.rep.get_top5())
        p1 = "asd"
        s1 = 0
        print("asd", self.rep.check_if_highscore(123))
        print("asd", self.rep.check_if_highscore(1))
        print(self.rep.add_new_highscore(p1, s1))
        print(self.rep.get_top5())

