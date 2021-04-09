
from score_repository import ScoreRepository
from game2048 import Game2048
import pygame as pg
import os
from ui.game_view import GameView
import time

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)

class Userinterface:
    """Luokka, jonka avulla pelin käyttöliittymä toimii.
    Attrbutes:
            game: uusi peli, 
            rep: Pisteiden hallinta
    """
    def __init__(self):
        """Luokan konstruktori, joka käynnistää pelin.
        """
        self.size = 4
        self.cell_size = 80
        self.screen_size = (self.size*self.cell_size + 2*self.cell_size + 300,
                            self.size*self.cell_size + 2*self.cell_size)
        self.game = Game2048(self.size)
        self.game_view = None
        self.game.add_new_tile()
        self.rep = ScoreRepository()

    def get_game_view(self, screen):
        self.game_view = GameView(self.game, self.cell_size, self.screen_size)
        screen.fill((0, 0, 200))
        self.game_view.all_sprites.draw(screen)
        pg.display.flip()

    def execute(self):
        pg.init()
        screen = pg.display.set_mode(self.screen_size)
        pg.display.set_caption("2048")
        clock = pg.time.Clock()

        self.get_game_view(screen)
        buttons = self.game_view.buttons

        auto_play = False
        auto_counter = 0
        pressed = False
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in buttons:
                        if button.rect.collidepoint(mouse_pos):
                            if button.tag == "b_up":
                                self.game.move_up()
                                pressed = True
                                auto_play = False
                            if button.tag == "b_down":
                                self.game.move_down()
                                pressed = True
                                auto_play = False
                            if button.tag == "b_right":
                                self.game.move_right()
                                pressed = True
                                auto_play = False
                            if button.tag == "b_left":
                                self.game.move_left()
                                pressed = True
                                auto_play = False
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.game.move_left()
                        pressed = True
                        auto_play = False
                    if event.key == pg.K_RIGHT:
                        self.game.move_right()
                        pressed = True
                        auto_play = False
                    if event.key == pg.K_UP:
                        self.game.move_up()
                        pressed = True
                        auto_play = False
                    if event.key == pg.K_DOWN:
                        self.game.move_down()
                        pressed = True
                        auto_play = False
                    if event.key == pg.K_SPACE:
                        if auto_play:
                            auto_play = False
                        else:
                            auto_play = True
                        time.sleep(0.1)

            if auto_play:
                auto_counter += 1
            if pressed:
                self.get_game_view(screen)
                pressed = False
            if auto_play:
                if auto_counter == 0:
                    self.game.move_down()
                    self.get_game_view(screen)
                if auto_counter == 1:
                    self.game.move_left()
                    self.get_game_view(screen)
                if auto_counter == 2:
                    self.game.move_up()
                    self.get_game_view(screen)
                if auto_counter == 3:
                    self.game.move_right()
                    self.get_game_view(screen)
                    auto_counter = -1

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

