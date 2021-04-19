
from repositories.score_repository import ScoreRepository
from game_logic.game2048 import Game2048
import pygame as pg
import os
from ui.game_view import GameView
import time
import PIL.Image
import PIL.ImageFilter
from screeninfo import get_monitors
from ui.menu_view import MenuView
from ui.game_files import GameFiles

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


class Userinterface:
    """Luokka, jonka avulla pelin käyttöliittymä toimii.
    Attrbutes:
            game: uusi peli, 
            rep: Pisteiden hallinta
    """

    def __init__(self):
        """Luokan konstruktori, joka käynnistää pelin.
        """
        pg.init()
        self.game = None
        self.cell_size = 80
        self.screen_size = ()
        self.game_view = None
        self.menu_view = None
        self.current_scene = "menu"
        self.end = False
        self.files = GameFiles()
        # self.rep = ScoreRepository()

    def get_game_view(self, screen, pop_up_tag=None, pop_up_b=None):
        self.game_view = GameView(
            self.game, self.cell_size, self.screen_size, self.files)
        screen.fill((0, 0, 200))
        self.update_screen(screen, pop_up_tag, pop_up_b)

    def update_screen(self, screen, pop_up_tag=None, pop_up_b=None):
        if self.current_scene == "game":
            self.game_view.all_sprites.draw(screen)
            if pop_up_tag is not None:
                screen.blit(self.get_blur(screen), (0, 0))
                self.game_view.update_pop_ups(pop_up_tag, {pop_up_b})
                self.game_view.pop_ups.draw(screen)
                self.game_view.pop_up_buttons.draw(screen)
        elif self.current_scene == "menu":
            self.menu_view.all_sprites.draw(screen)
        pg.display.flip()

    def press_button_anim(self, button_tag: str, screen, sleep_time=0.02):
        if self.current_scene == "game":
            self.game_view.update_buttons({button_tag})
        elif self.current_scene == "menu":
            self.menu_view.update_buttons({button_tag})
        self.update_screen(screen)
        time.sleep(sleep_time)

    def testi_run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            # pg.init()
            screen = pg.display.set_mode((400, 200))
            # window.position = (0,0)
            screen.fill((0, 0, 0))
            pg.display.flip()
            time.sleep(2)
            break
        pg.quit()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            screen = pg.display.set_mode((800, 100))
            # window.position = (0,0)
            screen.fill((100, 100, 100))
            pg.display.flip()

    def execute(self):
        monitors = get_monitors()
        x, y = monitors[0].width // 5, monitors[0].height // 5
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
        pg.display.set_caption("2048")
        self.execute_menu()
        # print("0")
        # while True:
        #     print("loop")
        #     if not self.end:
        #         print("1")
        #         pg.init()
        #         self.execute_game(8)
        #         print("2")
        #     else:
        #         break
        # # pg.quit()
        # # pg.init()
        # for i in range(10):
        #     print(i)
        # pg.quit()
        # pg.init()
        # self.asd(4)

    def asd(self, game_size):
        self.game = Game2048(game_size)
        self.game.add_new_tile()
        self.screen_size = (game_size*self.cell_size + 2*self.cell_size + 300,
                            game_size*self.cell_size + 2*self.cell_size)
        screens = pg.display.set_mode(self.screen_size)
        pg.display.set_caption("2048")
        clock = pg.time.Clock()
        self.get_game_view(screens)
        # buttons = self.game_view.buttons
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            screen = pg.display.set_mode((800, 100))
            screen.fill((100, 100, 100))
            pg.display.flip()

    def get_menu_view(self, screen):
        self.menu_view = MenuView(self.screen_size, self.files)
        screen.fill((0, 0, 200))
        self.update_screen(screen)

    def execute_menu(self):
        self.current_scene = "menu"
        self.screen_size = (720, 480)
        screen = pg.display.set_mode(self.screen_size)
        clock = pg.time.Clock()
        self.get_menu_view(screen)

        buttons = self.menu_view.buttons
        pressed = False
        new_scene = None
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in buttons:
                        if button.rect.collidepoint(mouse_pos):
                            if button.tag == "b_play":
                                new_scene = "game"
                            if button.tag == "b_scores":
                                # new_scene = "scores"
                                pass
                            if button.tag == "b_quit":
                                new_scene = "quit"
                            pressed = True
                            self.press_button_anim(button.tag, screen)
            if pressed:
                self.get_menu_view(screen)
                pressed = False
                if new_scene is not None:
                    break
            clock.tick(25)

        if new_scene == "game":
            self.execute_game(4)
        elif new_scene == "scores":
            # TODO score scene
            pass
        elif new_scene == "quit":
            exit()

    def execute_game(self, game_size):
        self.current_scene = "game"
        self.game = Game2048(game_size)
        self.game.add_new_tile()
        self.screen_size = (game_size*self.cell_size + 2*self.cell_size + 300,
                            game_size*self.cell_size + 2*self.cell_size)
        screen = pg.display.set_mode(self.screen_size)
        clock = pg.time.Clock()

        self.get_game_view(screen)
        buttons = self.game_view.buttons

        auto_play = False
        auto_counter = 0
        pressed = False
        pop_up_tag = None
        event = False

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    # self.end = True
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    if pop_up_tag is not None:
                        pop_up_buttons = self.game_view.pop_up_buttons
                        for button in pop_up_buttons:
                            if button.rect.collidepoint(mouse_pos):
                                if button.tag == "b_no":
                                    self.get_game_view(
                                        screen, pop_up_tag, button.tag)
                                    time.sleep(0.08)
                                    pressed = True
                                    pop_up_tag = None
                                if button.tag == "b_yes":
                                    self.end = True
                                    self.get_game_view(
                                        screen, pop_up_tag, button.tag)
                                    time.sleep(0.08)
                                    pressed = True
                                    if pop_up_tag == "restart" or pop_up_tag == "menu":
                                        event = pop_up_tag
                                        break
                        if event is not None:
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

            if event == "restart":
                self.game.add_new_tile()
                self.execute_game(game_size)
            elif event == "menu":
                self.execute()

            clock.tick(25)

    def get_blur(self, screen, img_mode="RGBA"):
        img = pg.image.tostring(screen, img_mode)
        img = PIL.Image.frombytes(img_mode, self.screen_size, img).filter(
            PIL.ImageFilter.GaussianBlur(radius=6))
        return pg.image.fromstring(img.tobytes("raw", img_mode), self.screen_size, img_mode)

    def execute_test(self):
        print(self.rep.get_top5())
        pelaajat = [("Mixu", 123), ("Pelaaja2", 12),
                    ("ASDSADSAd", 1233451), ("Testi1", 1233)]
        for pelaaja in pelaajat:
            print(self.rep.add_new_highscore(pelaaja[0], pelaaja[1]))
        print(self.rep.get_top5())
        p1 = "asd"
        s1 = 0
        print("asd", self.rep.check_if_highscore(123))
        print("asd", self.rep.check_if_highscore(1))
        print(self.rep.add_new_highscore(p1, s1))
        print(self.rep.get_top5())
