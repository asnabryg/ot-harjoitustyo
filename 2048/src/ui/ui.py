
from repositories.score_repository import ScoreRepository
from game_logic.game2048 import Game2048
import pygame as pg
import os
from ui.game_view import GameView
import time
import PIL.Image
import PIL.ImageFilter
from screeninfo import get_monitors
from ui.highscore_view import HighscoreView
from ui.menu_view import MenuView
from ui.game_files import GameFiles
from ui.score_saving_view import ScoreSavingView

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


class Userinterface:
    """Luokka, jonka avulla pelin käyttöliittymä toimii.
    """

    def __init__(self):
        """Luokan konstruktori, joka alustaa muuttujia.
        """
        pg.init()
        self.game = None
        self.can_move = (True, True, True, True)  # (up, down, right, left)
        self.cell_size = 80
        self.screen_size = ()
        self.game_view = None
        self.menu_view = None
        self.highscore_view = None
        self.current_scene = "menu"
        self.end = False
        self.board_size = None
        self.score_saving_view = None
        self.files = GameFiles()
        self.rep = ScoreRepository()
        self.pre_highscore = 0
        self.background_color = (3, 57, 108)

    def get_game_view(self, screen, pop_up_tag=None, pop_up_b=None):
        """Hakee kaikki spritet valmiiksi, mitä Peli ruudussa tarvitaan.

        Args:
            screen (pygame.display): pygamen näyttö
            pop_up_tag (str, valinnainen): Pop_up ikkunan tag. Oletus: None.
            pop_up_b (set(), valinnainen): Painetun napin tag. Oletus: None.
        """
        self.game_view = GameView(
            self.game, self.cell_size, self.screen_size, self.files, self.pre_highscore, self.can_move)
        screen.fill(self.background_color)
        self.update_screen(screen, pop_up_tag, pop_up_b)

    def update_screen(self, screen, pop_up_tag=None, pop_up_b=None):
        """Renderöi ruudulle kaikki spritet, jotka haettu.

        Args:
            screen (pygame.display): pygamen näyttö
            pop_up_tag (str, valinnainen): Pop_up ikkunan tag. Oletus: None.
            pop_up_b (set(), valinnainen): Painetun napin tag. Oletus: None.
        """
        if self.current_scene == "game":
            self.game_view.all_sprites.draw(screen)
            if pop_up_tag is not None:
                screen.blit(self.get_blur(screen), (0, 0))
                self.game_view.update_pop_ups(pop_up_tag, {pop_up_b})
                self.game_view.pop_ups.draw(screen)
                self.game_view.pop_up_buttons.draw(screen)
        elif self.current_scene == "menu":
            self.menu_view.all_sprites.draw(screen)
            if pop_up_tag is not None:
                screen.blit(self.get_blur(screen), (0, 0))
                self.menu_view.update_pop_ups(pop_up_tag, {pop_up_b})
                self.menu_view.pop_ups.draw(screen)
                self.menu_view.pop_up_buttons.draw(screen)
        elif self.current_scene == "highscores":
            self.highscore_view.all_sprites.draw(screen)
        pg.display.flip()

    def press_button_anim(self, button_tag: str, screen, sleep_time=0.02):
        """Hakee nappi spritet, mutta painettuina.

        Args:
            button_tag (str): Napin tag, joka painettu.
            screen (pygame.display): pygamen näyttö.
            sleep_time (float, valinnainen): Kuinka kauan napin painus kestää. Oletus: 0.02.
        """
        if self.current_scene == "game":
            self.game_view.update_buttons({button_tag})
        elif self.current_scene == "menu":
            self.menu_view.update_buttons({button_tag})
        elif self.current_scene == "highscores":
            self.highscore_view.update_buttons({button_tag})
        self.update_screen(screen)
        time.sleep(sleep_time)

    def execute(self):
        """Metodi, joka käynnistää pelin.
        """
        monitors = get_monitors()
        x, y = monitors[0].width // 5, monitors[0].height // 5
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
        pg.display.set_caption("2048")
        self.score_saving_view = None
        self.execute_menu()

    def get_menu_view(self, screen, pop_up_tag=None, pop_up_b=None):
        """Hakee kaikki spritet valmiiksi, mitä Menu -valikossa tarvitaan.

        Args:
            screen (pygame.display): pygamen näyttö
            pop_up_tag (str, valinnainen): Pop_up ikkunan tag. Oletus: None.
            pop_up_b (set(), valinnainen): Painetun napin tag. Oletus: None.
        """
        self.menu_view = MenuView(self.screen_size, self.files)
        screen.fill(self.background_color)
        self.update_screen(screen, pop_up_tag, pop_up_b)

    def execute_menu(self):
        """Metodi, joka suorittaa Menu -valikon käyttöliittymän.
        """
        self.current_scene = "menu"
        self.screen_size = (720, 480)
        screen = pg.display.set_mode(self.screen_size)
        clock = pg.time.Clock()
        self.get_menu_view(screen)
        self.can_move = (True, True, True, True)

        buttons = self.menu_view.buttons
        pressed = False
        new_scene = None
        pop_up_tag = None

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if pop_up_tag is not None:
                        pop_up_buttons = self.menu_view.pop_up_buttons
                        for button in pop_up_buttons:
                            if button.rect.collidepoint(mouse_pos):
                                self.get_menu_view(
                                    screen, pop_up_tag, button.tag)
                                time.sleep(0.08)
                                pressed = True
                                if button.tag == "b_4x4":
                                    new_scene = ("game", 4)
                                elif button.tag == "b_5x5":
                                    new_scene = ("game", 5)
                                elif button.tag == "b_6x6":
                                    new_scene = ("game", 6)
                                elif button.tag == "b_back":
                                    pop_up_tag = None
                    else:
                        for button in buttons:
                            if button.rect.collidepoint(mouse_pos) and pop_up_tag is None:
                                if button.tag == "b_play":
                                    pop_up_tag = "play"
                                if button.tag == "b_scores":
                                    new_scene = ("scores",)
                                if button.tag == "b_quit":
                                    new_scene = ("quit",)
                                pressed = True
                                self.press_button_anim(button.tag, screen)
            if pressed:
                self.get_menu_view(screen, pop_up_tag)
                pressed = False
                if new_scene is not None:
                    break
            clock.tick(25)

        if new_scene[0] == "game":
            self.board_size = new_scene[1]
            self.pre_highscore = self.rep.get_highscore(self.board_size)
            self.execute_game(self.board_size)
        elif new_scene[0] == "scores":
            self.execute_highscores()
        elif new_scene[0] == "quit":
            exit()

    def get_score_saving_view(self, screen, background, b_press=set(), char="", backspace=False, is_highscore=True):
        """Hakee kaikki spritet valmiiksi, mitä ScoreSavingView -pop-up ikkunassa tarvitaan,
        ja päivittää ruudun.

        Args:
            screen (pygame.display): pygamen näyttö.
            background (pygame.image): taustakuva
            b_press (set(), valinnainen): Napit joita painettu.
            char (str): Näppäimistön Painetun näppäimistö napin kirjain tai numero. 
            backspace (bool): True, jos painettu 'backspace' näppäintä.
            is_highscore (bool): True, jos on uusi ennätys.
        """
        if self.score_saving_view is None:
            screen.blit(background, (0, 0))
            self.score_saving_view = ScoreSavingView(
                self.files, self.screen_size, self.game.get_score(), is_highscore)
            self.score_saving_view.pop_ups.draw(screen)
            self.score_saving_view.texts.draw(screen)
        if is_highscore:
            self.score_saving_view.update_name(char, backspace)
            self.score_saving_view.name_surface.draw(screen)
        self.score_saving_view.update_buttons(b_press)
        self.score_saving_view.buttons.draw(screen)
        pg.display.flip()

    def execute_score_saving(self, screen, background, is_highscore):
        """Metodi, joka suorittaa pop-up ikkunan käyttöliittymän, kun peli päättyy.

        Args:
            screen (pygame.display): pygamen näyttö
            background (pygame.image): taustakuva
            is_highscore (bool): True, jos on uusi ennätys.
        """
        self.get_score_saving_view(
            screen, background, is_highscore=is_highscore)
        pressed = False
        chars = "abcdefghijklmnopqrstuvwxyzåäö"
        chars = chars + chars.upper() + " 1234567890_"
        char = ""
        backspace = False
        event_scene = ""
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    buttons = self.score_saving_view.buttons
                    for button in buttons:
                        if button.rect.collidepoint(mouse_pos):
                            if button.tag == "b_submit":
                                if self.score_saving_view.name.strip() != "":
                                    self.get_score_saving_view(
                                        screen, background, {button.tag}, is_highscore=is_highscore)
                                    pressed = True
                                    time.sleep(0.08)
                                    event_scene = "submit"
                            if button.tag == "b_menu":
                                self.get_score_saving_view(
                                    screen, background, {button.tag}, is_highscore=is_highscore)
                                pressed = True
                                time.sleep(0.08)
                                event_scene = "menu"
                            if button.tag == "b_restart":
                                self.get_score_saving_view(
                                    screen, background, {button.tag}, is_highscore=is_highscore)
                                pressed = True
                                time.sleep(0.08)
                                event_scene = "restart"
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_BACKSPACE:
                        pressed = True
                        char = ""
                        backspace = True
                    elif event.unicode in chars:
                        pressed = True
                        char = event.unicode
                        backspace = False
            if pressed:
                pressed = False
                self.get_score_saving_view(
                    screen, background, char=char, backspace=backspace, is_highscore=is_highscore)
                char = ""
                backspace = False
            if event_scene == "submit":
                self.rep.add_new_highscore(
                    self.score_saving_view.name, self.game.get_score(), self.board_size)
                self.score_saving_view = None
                self.pre_highscore = self.rep.get_highscore(self.board_size)
                self.execute()
            elif event_scene == "menu":
                self.score_saving_view = None
                self.pre_highscore = self.rep.get_highscore(self.board_size)
                self.execute()
            elif event_scene == "restart":
                self.score_saving_view = None
                self.pre_highscore = self.rep.get_highscore(self.board_size)
                self.execute_game(self.board_size)

    def get_highscore_view(self, screen, btns_down={"b_4x4"}):
        """Hakee kaikki spritet valmiiksi, mitä Highscore -valikossa tarvitaan.

        Args:
            screen (pygame.display): pygamen näyttö
            btns_down (set): Painetun napin tag.
        """
        score_list = []
        if "b_4x4" in btns_down:
            score_list = self.rep.get_top5(4)
        elif "b_5x5" in btns_down:
            score_list = self.rep.get_top5(5)
        elif "b_6x6" in btns_down:
            score_list = self.rep.get_top5(6)
        self.highscore_view = HighscoreView(
            self.screen_size, self.rep, self.files, score_list, btns_down)
        screen.fill(self.background_color)
        self.update_screen(screen)

    def execute_highscores(self):
        """Metodi, joka suorittaa Highscore -valikon käyttöliittymän.
        """
        self.current_scene = "highscores"
        screen = pg.display.set_mode(self.screen_size)
        clock = pg.time.Clock()
        self.get_highscore_view(screen)

        buttons = self.highscore_view.buttons
        pressed = False
        back = False

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in buttons:
                        if button.rect.collidepoint(mouse_pos):
                            if button.tag == "b_back":
                                back = True
                            self.get_highscore_view(screen, {button.tag})
                    if back:
                        break
            if pressed:
                pressed = False
            if back:
                break
            clock.tick(25)
        self.execute_menu()

    def execute_game(self, game_size):
        """Metodi, joka suorittaa pelin pelaamisen käyttöliittymän.

        Args:
            game_size (int): Pelialueen koko.
        """
        self.current_scene = "game"
        self.game = Game2048(game_size)
        self.game.add_new_tile()
        self.screen_size = (game_size*self.cell_size + 2*self.cell_size + 300,
                            game_size*self.cell_size + 2*self.cell_size)
        screen = pg.display.set_mode(self.screen_size)
        clock = pg.time.Clock()

        self.get_game_view(screen)
        buttons = self.game_view.buttons

        pressed = False
        pop_up_tag = None
        event = False

        while True:
            if self.game.is_gameover():
                # GAMEOVER
                # Tallennetaan tulos
                score = self.game.get_score()
                self.execute_score_saving(screen, self.get_blur(
                    screen), self.rep.check_if_highscore(score, self.board_size))
            else:
                # GAME
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
                                    if pop_up_tag is None:
                                        if button.tag == "b_restart":
                                            self.press_button_anim(
                                                "b_restart", screen)
                                            pop_up_tag = "restart"
                                            pressed = True
                                        if button.tag == "b_menu":
                                            self.press_button_anim(
                                                "b_menu", screen)
                                            pop_up_tag = "menu"
                                            pressed = True

                                        if button.tag == "b_up" and self.can_move[0]:
                                            self.press_button_anim(
                                                "b_up", screen)
                                            self.game.move("up")
                                            pressed = True
                                        if button.tag == "b_down" and self.can_move[1]:
                                            self.press_button_anim(
                                                "b_down", screen)
                                            self.game.move("down")
                                            pressed = True
                                        if button.tag == "b_right" and self.can_move[2]:
                                            self.press_button_anim(
                                                "b_right", screen)
                                            self.game.move("right")
                                            pressed = True
                                        if button.tag == "b_left" and self.can_move[3]:
                                            self.press_button_anim(
                                                "b_left", screen)
                                            self.game.move("left")
                                            pressed = True

                    if event.type == pg.KEYDOWN:
                        if pop_up_tag is None:
                            if event.key == pg.K_LEFT and self.can_move[3]:
                                self.press_button_anim("b_left", screen)
                                self.game.move("left")
                                pressed = True
                            if event.key == pg.K_RIGHT and self.can_move[2]:
                                self.press_button_anim("b_right", screen)
                                self.game.move("right")
                                pressed = True
                            if event.key == pg.K_UP and self.can_move[0]:
                                self.press_button_anim("b_up", screen)
                                self.game.move("up")
                                pressed = True
                            if event.key == pg.K_DOWN and self.can_move[1]:
                                self.press_button_anim("b_down", screen)
                                self.game.move("down")
                                pressed = True

                if pressed:
                    # (up, down, right, left)
                    self.can_move = (self.game.move("up", check_if_can_move=True),
                                     self.game.move("down",
                                                    check_if_can_move=True),
                                     self.game.move("right",
                                                    check_if_can_move=True),
                                     self.game.move("left", check_if_can_move=True))
                    if not self.can_move[0] and not self.can_move[1] and not self.can_move[2] and not self.can_move[3]:
                        # Gameover
                        if self.game._check_if_gameover():
                            self.game._game_over = True
                    self.get_game_view(screen, pop_up_tag)
                    pressed = False

                if event == "restart":
                    self.pre_highscore = self.rep.get_highscore(
                        self.board_size)
                    self.execute_game(self.board_size)
                elif event == "menu":
                    self.execute_score_saving(screen, self.get_blur(
                        screen), self.rep.check_if_highscore(self.game.get_score(), self.board_size))
            clock.tick(25)

    def get_blur(self, screen, img_mode="RGBA"):
        """Metodi sumentaa näytön kuvan ja palauttaa sen string muodossa.

        Args:
            screen (pygame.display): pygamen näyttö
            img_mode (str, valinnainen): Kuvan värimalli. Oletus: "RGBA".

        Returns:
            str: summennetun näytön kuva string muodossa.
        """
        img = pg.image.tostring(screen, img_mode)
        img = PIL.Image.frombytes(img_mode, self.screen_size, img).filter(
            PIL.ImageFilter.GaussianBlur(radius=6))
        return pg.image.fromstring(img.tobytes("raw", img_mode), self.screen_size, img_mode)
