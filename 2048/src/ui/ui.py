
from score_repository import ScoreRepository
from game2048 import Game2048
import pygame as pg
import os
from ui.game_view import GameView

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
        """Luokan konstruktori, joka käynnistää pelin
        """
        self.game = Game2048(4)
        self.game.add_new_tile()
        self.rep = ScoreRepository()

    def get_game_view(self, screen):
        game = GameView(self.game)
        screen.fill((0, 0, 200))
        game.all_sprites.draw(screen)
        pg.display.flip()

    def execute(self):
        pg.init()
        screen = pg.display.set_mode((640, 480))
        pg.display.set_caption("2048")
        clock = pg.time.Clock()

        self.get_game_view(screen)

        pressed = False
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.game.move_left()
                        pressed = True
                    if event.key == pg.K_RIGHT:
                        self.game.move_right()
                        pressed = True
                    if event.key == pg.K_UP:
                        self.game.move_up()
                        pressed = True
                    if event.key == pg.K_DOWN:
                        self.game.move_down()
                        pressed = True
            
            if pressed:
                self.get_game_view(screen)
                pressed = False

            clock.tick(25)

    def execute_test(self):
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

