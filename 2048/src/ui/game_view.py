
import pygame as pg
from pygame.transform import rotate
from ui.tile import Tile
from ui.text import Text
from ui.button import Button
from game2048 import Game2048

class GameView():
    """Luokka, jossa alustetaan pelilaudan sprite näytölle.
    """

    def __init__(self, game: Game2048, cell_size, screen_size):
        """Luokan konstruktori.

        Args:
            game (Game2048): Peli
            cell_size (int): Peli laattojen koko
            screen_size (tuple): Näytön leveys ja korkeus
        """
        self.game = game
        self.screen_size = screen_size
        self.tiles = pg.sprite.Group()
        self.texts = pg.sprite.Group()
        self.buttons = pg.sprite.Group()
        self.cell_size = cell_size
        self.all_sprites = pg.sprite.Group()
        self.m_x = (310//6)
        self.m_y = (240//2)
        self.initialize()

    def initialize(self):
        """Luo sprite ryhmän, jossa pelilaatat on asetettu järjestykseen.
        """
        board = self.game.get_board()
        size = self.game.get_size()

        score = self.game.get_score()
        text = "Score: " + str(score)
        margin = 15
        score_x = self.m_x + margin
        score_y = self.m_y - (self.cell_size - margin)
        self.texts.add(Text(text, score_x, score_y, 35, (255, 255, 255), self.cell_size*self.game.get_size() - margin*2, 50, (0, 0, 180)))

        for y in range(size):
            for x in range(size):
                cell = board[y][x]
                normalized_x = x * self.cell_size + self.m_x
                normalized_y = y * self.cell_size + self.m_y

                self.tiles.add(Tile(0, normalized_x, normalized_y, self.cell_size))  # tausta
                if cell == 0:
                    continue
                self.tiles.add(Tile(cell, normalized_x, normalized_y, self.cell_size))  # tile


        self.update_buttons()

        self.all_sprites.add(self.tiles, self.texts)
    
    def update_buttons(self, b_press=set()):
        b_size = 70
        x = self.m_x + self.cell_size * self.game.get_size()
        y = self.cell_size * self.game.get_size()

        b_press_up_color = (0, 0, 220)
        b_press_down_color = (0, 0, 100)

        if "b_up" in b_press:
            b_color = b_press_down_color
        else:
            b_color = b_press_up_color
        b_up = Button(tag="b_up",
                      text=None,
                      text_color=None,
                      img_file="button_up.png",
                      b_color=b_color,
                      position=((((self.screen_size[0] - x) // 2) + x) - (b_size // 2),
                                (self.m_y + y // 2) - b_size * 1.5),
                      size=(b_size, b_size),
                      rotate=0)

        if "b_down" in b_press:
            b_color = b_press_down_color
        else:
            b_color = b_press_up_color
        b_down = Button(tag="b_down",
                        text=None,
                        text_color=None,
                        img_file="button_up.png",
                        b_color=b_color,
                        position=((((self.screen_size[0] - x) // 2) + x) - (b_size // 2),
                                  (self.m_y + y // 2) - b_size * 1.5 + b_size * 2),
                        size=(b_size, b_size),
                        rotate=180)
        
        if "b_right" in b_press:
            b_color = b_press_down_color
        else:
            b_color = b_press_up_color
        b_right = Button(tag="b_right",
                         text=None,
                         text_color=None,
                         img_file="button_up.png",
                         b_color=b_color,
                         position=((((self.screen_size[0] - x) // 2) + x) - (b_size // 2) + b_size,
                                   (self.m_y + y // 2) - b_size * 1.5 + b_size),
                         size=(b_size, b_size),
                         rotate=-90)

        if "b_left" in b_press:
            b_color = b_press_down_color
        else:
            b_color = b_press_up_color
        b_left = Button(tag="b_left",
                        text=None,
                        text_color=None,
                        img_file="button_up.png",
                        b_color=b_color,
                        position=((((self.screen_size[0] - x) // 2) + x) - (b_size // 2) - b_size,
                                  (self.m_y + y // 2) - b_size * 1.5 + b_size),
                        size=(b_size, b_size),
                        rotate=90)

        self.buttons.add(b_up)
        self.buttons.add(b_down)
        self.buttons.add(b_right)
        self.buttons.add(b_left)

        self.all_sprites.add(self.buttons)

