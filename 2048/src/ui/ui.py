
from score_repository import ScoreRepository
from game2048 import Game2048
import pygame as pg
import os
from ui.game_view import GameView
import time
import PIL.Image
import PIL.ImageFilter

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
        self.size = 5
        self.cell_size = 80
        self.screen_size = (self.size*self.cell_size + 2*self.cell_size + 300,
                            self.size*self.cell_size + 2*self.cell_size)
        self.game = Game2048(self.size)
        self.game_view = None
        self.game.add_new_tile()
        self.rep = ScoreRepository()

    def get_game_view(self, screen, pop_up_tag=None, pop_up_b=None):
        self.game_view = GameView(self.game, self.cell_size, self.screen_size)
        screen.fill((0, 0, 200))
        self.update_screen(screen, pop_up_tag, pop_up_b)
    
    def update_screen(self, screen, pop_up_tag=None, pop_up_b=None):
        self.game_view.all_sprites.draw(screen)
        if pop_up_tag is not None:
            screen.blit(self.get_blur(screen), (0, 0))
            self.game_view.update_pop_ups(pop_up_tag, {pop_up_b})
            self.game_view.pop_ups.draw(screen)
            self.game_view.pop_up_buttons.draw(screen)
        pg.display.flip()
    
    def press_button_anim(self, button_tag: str, screen, sleep_time=0.02):
        self.game_view.update_buttons({button_tag})
        self.update_screen(screen, None)
        time.sleep(sleep_time)

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
        pop_up_tag = None
        restart = False
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if pop_up_tag is not None:
                        pop_up_buttons = self.game_view.pop_up_buttons
                        for button in pop_up_buttons:
                            if button.rect.collidepoint(mouse_pos):
                                if button.tag == "b_no":
                                    self.get_game_view(screen, pop_up_tag, button.tag)
                                    time.sleep(0.08)
                                    pressed = True
                                    pop_up_tag = None
                                if button.tag == "b_yes":
                                    if pop_up_tag == "restart":
                                        restart = True
                                        break
                        if restart:
                            break

                    else:
                        for button in buttons:
                            if button.rect.collidepoint(mouse_pos):
                                if button.tag == "b_restart" and pop_up_tag is None:
                                    self.press_button_anim("b_restart", screen)
                                    pop_up_tag = "restart"
                                    auto_play = False
                                    pressed = True
                                if button.tag == "b_menu" and pop_up_tag is None:
                                    self.press_button_anim("b_menu", screen)
                                    pop_up_tag = "menu"
                                    auto_play = False
                                    pressed = True

                                if button.tag == "b_up" and pop_up_tag is None:
                                    self.press_button_anim("b_up", screen)
                                    self.game.move_up()
                                    pressed = True
                                    auto_play = False
                                if button.tag == "b_down" and pop_up_tag is None:
                                    self.press_button_anim("b_down", screen)
                                    self.game.move_down()
                                    pressed = True
                                    auto_play = False
                                if button.tag == "b_right" and pop_up_tag is None:
                                    self.press_button_anim("b_right", screen)
                                    self.game.move_right()
                                    pressed = True
                                    auto_play = False
                                if button.tag == "b_left" and pop_up_tag is None:
                                    self.press_button_anim("b_left", screen)
                                    self.game.move_left()
                                    pressed = True
                                    auto_play = False
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT and pop_up_tag is None:
                        self.press_button_anim("b_left", screen)
                        self.game.move_left()
                        pressed = True
                        auto_play = False
                    if event.key == pg.K_RIGHT and pop_up_tag is None:
                        self.press_button_anim("b_right", screen)
                        self.game.move_right()
                        pressed = True
                        auto_play = False
                    if event.key == pg.K_UP and pop_up_tag is None:
                        self.press_button_anim("b_up", screen)
                        self.game.move_up()
                        pressed = True
                        auto_play = False
                    if event.key == pg.K_DOWN and pop_up_tag is None:
                        self.press_button_anim("b_down", screen)
                        self.game.move_down()
                        pressed = True
                        auto_play = False
                    if event.key == pg.K_SPACE and pop_up_tag is None:
                        if auto_play:
                            auto_play = False
                        else:
                            auto_play = True
                        time.sleep(0.02)
            
            if restart:
                self.game = Game2048(self.size)
                self.game.add_new_tile()
                self.execute()

            if auto_play:
                auto_counter += 1
            if pressed:
                self.get_game_view(screen, pop_up_tag)
                pressed = False
            if auto_play:
                if auto_counter == 0:
                    self.press_button_anim("b_down", screen, 0)
                    self.game.move_down()
                    self.get_game_view(screen)
                if auto_counter == 1:
                    self.press_button_anim("b_left", screen, 0)
                    self.game.move_left()
                    self.get_game_view(screen)
                if auto_counter == 2:
                    self.press_button_anim("b_up", screen, 0)
                    self.game.move_up()
                    self.get_game_view(screen)
                if auto_counter == 3:
                    self.press_button_anim("b_right", screen, 0)
                    self.game.move_right()
                    self.get_game_view(screen)
                    auto_counter = -1

            clock.tick(25)

        if restart:
            pass
            
    def get_blur(self, screen, img_mode="RGBA"):
        img = pg.image.tostring(screen, img_mode)
        img = PIL.Image.frombytes(img_mode, self.screen_size, img).filter(PIL.ImageFilter.GaussianBlur(radius=6))
        return pg.image.fromstring(img.tobytes("raw", img_mode), self.screen_size, img_mode)

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

