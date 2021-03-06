
import pygame as pg
from ui.tile import Tile
from ui.text import Text
from ui.button import Button
from game_logic.game2048 import Game2048


class GameView():
    """Luokka, jossa alustetaan pelilaudan sprite näytölle.
    """

    def __init__(self, game: Game2048, cell_size, screen_size, files, highscore, can_move=(True, True, True, True)):
        """Luokan konstruktori.

        Args:
            game (Game2048): Peli.
            cell_size (int): Peli laattojen koko.
            screen_size (tuple): Näytön leveys ja korkeus.
            files (GameFiles): Pelin tiedostot.
            highscore (int): Top1 tulos
            can_move (tuple): Kaikki suunnat mihin voi liikuttaa laattoja (up, down, right, left)
        """
        self.game = game
        self.can_move = can_move
        self.highscore = highscore
        self.screen_size = screen_size
        self.tiles = pg.sprite.Group()
        self.texts = pg.sprite.Group()
        self.buttons = pg.sprite.Group()
        self.pop_ups = pg.sprite.Group()
        self.pop_up_buttons = pg.sprite.Group()
        self.cell_size = cell_size
        self.all_sprites = pg.sprite.Group()
        self.m_x = (310//8)
        self.m_y = (240//2)
        self.files = files
        self.initialize()

    def initialize(self):
        """Luo sprite ryhmän, jossa pelilaatat on asetettu järjestykseen.
        """
        board = self.game.get_board()
        size = self.game.get_size()

        score = self.game.get_score()
        text = "Score: " + str(score)
        margin = 15
        W = self.cell_size*self.game.get_size() - margin*2
        score_x = self.m_x + margin
        score_y = self.m_y - (self.cell_size - margin)
        self.texts.add(Text(text, score_x, score_y, 30, (255, 255, 255),
                       W, 50, (5, 41, 85)))

        text = "Best score: " + str(self.highscore)
        margin = 15
        score_x = self.m_x + self.cell_size*self.game.get_size() + margin
        score_y = self.m_y - (self.cell_size - margin)
        self.texts.add(Text(text, score_x, score_y, 30, (255, 255, 255),
                       self.screen_size[0] - score_x - margin, 50, (5, 41, 85)))

        for y in range(size):
            for x in range(size):
                value = board[y][x]
                normalized_x = x * self.cell_size + self.m_x
                normalized_y = y * self.cell_size + self.m_y

                self.tiles.add(Tile(0, normalized_x, normalized_y, self.cell_size, color=None,
                               image=self.files.get_tile0_img_str(), files=self.files))  # tausta
                if value == 0:
                    continue
                self.tiles.add(
                    Tile(value, normalized_x, normalized_y, self.cell_size, color=None, image=self.files.get_tile_img_str(), files=self.files))  # tile

        self.update_buttons()

        self.all_sprites.add(self.tiles, self.texts)

    def update_buttons(self, b_press=set()):
        """Renderöi kaikki napit ja nappien värin vaihdon

        Args:
            b_press (set(str), valinnainen): Renderöi kaikki setissä olevat napit painetuiksi.
        """
        self.buttons.empty()
        # print(self.can_move)
        b_size = 70
        x = self.m_x + self.cell_size * self.game.get_size()
        y = self.cell_size * self.game.get_size()

        b_press_up_color = (15, 77, 138)
        b_press_down_color = (5, 60, 100)
        b_gray = (3, 57, 108)
        y_margin = 30

        if "b_up" in b_press:
            b_color = b_press_down_color
        else:
            if self.can_move[0]:
                b_color = b_press_up_color
            else:
                b_color = b_gray
        b_up = Button(tag="b_up",
                      text=None,
                      text_color=None,
                      img_file_str=self.files.get_button_up_img_str(),
                      b_color=b_color,
                      position=((((self.screen_size[0] - x) // 2) + x) - (b_size // 2),
                                (self.m_y + y // 2) - b_size * 1.5 + y_margin),
                      size=(b_size, b_size),
                      rotate=0)

        if "b_down" in b_press:
            b_color = b_press_down_color
        else:
            if self.can_move[1]:
                b_color = b_press_up_color
            else:
                b_color = b_gray
        b_down = Button(tag="b_down",
                        text=None,
                        text_color=None,
                        img_file_str=self.files.get_button_up_img_str(),
                        b_color=b_color,
                        position=((((self.screen_size[0] - x) // 2) + x) - (b_size // 2),
                                  (self.m_y + y // 2) - b_size * 1.5 + b_size * 2 + y_margin),
                        size=(b_size, b_size),
                        rotate=180)

        if "b_right" in b_press:
            b_color = b_press_down_color
        else:
            if self.can_move[2]:
                b_color = b_press_up_color
            else:
                b_color = b_gray
        b_right = Button(tag="b_right",
                         text=None,
                         text_color=None,
                         img_file_str=self.files.get_button_up_img_str(),
                         b_color=b_color,
                         position=((((self.screen_size[0] - x) // 2) + x) - (b_size // 2) + b_size,
                                   (self.m_y + y // 2) - b_size * 1.5 + b_size + y_margin),
                         size=(b_size, b_size),
                         rotate=-90)

        if "b_left" in b_press:
            b_color = b_press_down_color
        else:
            if self.can_move[3]:
                b_color = b_press_up_color
            else:
                b_color = b_gray
        b_left = Button(tag="b_left",
                        text=None,
                        text_color=None,
                        img_file_str=self.files.get_button_up_img_str(),
                        b_color=b_color,
                        position=((((self.screen_size[0] - x) // 2) + x) - (b_size // 2) - b_size,
                                  (self.m_y + y // 2) - b_size * 1.5 + b_size + y_margin),
                        size=(b_size, b_size),
                        rotate=90)

        self.buttons.add(b_up)
        self.buttons.add(b_down)
        self.buttons.add(b_right)
        self.buttons.add(b_left)

        if "b_restart" in b_press:
            b_color = (130, 10, 42)
        else:
            b_color = (183, 40, 72)
        b_restart = Button(tag="b_restart",
                           text="Restart",
                           text_color=(240, 240, 240),
                           img_file_str=self.files.get_button_img_str(),
                           b_color=b_color,
                           position=((((self.screen_size[0] - x) // 2) + x) - (90 // 2) - 90//1.5,
                                     self.m_y),
                           size=(90, 35),
                           rotate=0)

        if "b_menu" in b_press:
            b_color = (130, 10, 42)
        else:
            b_color = (183, 40, 72)
        b_menu = Button(tag="b_menu",
                        text="Menu",
                        text_color=(240, 240, 240),
                        img_file_str=self.files.get_button_img_str(),
                        b_color=b_color,
                        position=((((self.screen_size[0] - x) // 2) + x) - (90 // 2) + 90//1.5,
                                  self.m_y),
                        size=(90, 35),
                        rotate=0)

        self.buttons.add(b_restart)
        self.buttons.add(b_menu)

        self.all_sprites.add(self.buttons)

    def update_pop_ups(self, tag: str, b_press=set()):
        """Renderöi pop-up ikkunat näkyville tagin perusteella. Myös sen napit.

        Args:
            tag (str): mikä pop-up ikkuna halutaan näkyville.
            b_press (set(str), valinnainen): Renderöi kaikki setissä olevat napit painetuiksi.
        """
        size = (350, 250)
        x = (self.screen_size[0] - size[0]) // 2
        y = (self.screen_size[1] - size[1]) // 2
        restart_pop = Tile(0, x, y, color=(100, 100, 100))
        restart_pop.color = (230, 200, 200)
        restart_pop.image = pg.transform.scale(restart_pop.img, size)
        self.pop_ups.add(restart_pop)

        # Buttons:

        margin = 15
        b_size = (90, 35)
        if "b_yes" in b_press:
            b_color = (0, 100, 0)
        else:
            b_color = (0, 185, 78)
        b_yes = Button(tag="b_yes",
                       text="Yes",
                       text_color=(240, 240, 240),
                       img_file_str=self.files.get_button_img_str(),
                       b_color=b_color,
                       position=(x + size[0] // 2 - b_size[0] * 1.5 + 20,
                                 y + size[1] // 1.5),
                       size=b_size,
                       rotate=0)

        if "b_no" in b_press:
            b_color = (130, 10, 42)
        else:
            b_color = (183, 40, 72)
        b_no = Button(tag="b_no",
                      text="No",
                      text_color=(240, 240, 240),
                      img_file_str=self.files.get_button_img_str(),
                      b_color=b_color,
                      position=(x + size[0] // 2 + b_size[0] * .5 - 20,
                                y + size[1] // 1.5),
                      size=b_size,
                      rotate=0)

        self.pop_up_buttons.add(b_yes)
        self.pop_up_buttons.add(b_no)

        # Text:
        x = x + margin
        y = y + margin
        s = ""
        if tag == "restart":
            s = "Are you sure you want restart?"
        elif tag == "menu":
            s = "Return to the main menu?"
        text = Text(s,
                    x, y, 25, (255, 255, 255),
                    size[0] - margin * 2, 40, (100, 100, 100))

        self.pop_ups.add(text)
