
from typing import Text
import pygame as pg
from ui.button import Button
from ui.text import Text
from ui.tile import Tile


class MenuView:

    def __init__(self, screen_size, files):
        self.buttons = pg.sprite.Group()
        self.texts = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.screen_size = screen_size
        self.pop_ups = pg.sprite.Group()
        self.pop_up_buttons = pg.sprite.Group()
        self.files = files
        self.initialize()

    def initialize(self):
        surface_size = (400, 100)
        self.texts.add(Text(text="2048",
                            x=self.screen_size[0] // 2 - surface_size[0] // 2,
                            y=50,
                            size=120,
                            text_color=(255, 255, 255),
                            width=surface_size[0],
                            height=surface_size[1],
                            back_color=(0, 0, 200),
                            outline="fat",
                            outline_style="shadow"))

        self.all_sprites.add(self.texts)

        self.update_buttons()

    def update_buttons(self, b_press=set()):

        b_size = (150, 60)

        b_press_up_color = (0, 200, 0)
        b_press_down_color = (0, 100, 0)
        if "b_play" in b_press:
            b_color = b_press_down_color
        else:
            b_color = b_press_up_color
        b_play = Button(tag="b_play",
                        text="Play",
                        font=self.files.get_font(40),
                        text_color=(255, 255, 255),
                        img_file_str=self.files.get_button_img_str(),
                        b_color=b_color,
                        position=(self.screen_size[0] // 2 - b_size[0] // 2,
                                  self.screen_size[1] // 2.5),
                        size=b_size,
                        rotate=0)

        b_size = (150, 40)
        b_press_up_color = (0, 200, 0)
        b_press_down_color = (0, 100, 0)
        if "b_scores" in b_press:
            b_color = b_press_down_color
        else:
            b_color = b_press_up_color
        b_scores = Button(tag="b_scores",
                          text="Highscores",
                          font=self.files.get_font(30),
                          text_color=(255, 255, 255),
                          img_file_str=self.files.get_button_img_str(),
                          b_color=b_color,
                          position=(self.screen_size[0] // 2 - b_size[0] // 2,
                                    self.screen_size[1] // 1.8),
                          size=b_size,
                          rotate=0)

        b_size = (110, 35)
        b_press_up_color = (150, 0, 0)
        b_press_down_color = (50, 0, 0)
        if "b_quit" in b_press:
            b_color = b_press_down_color
        else:
            b_color = b_press_up_color
        b_quit = Button(tag="b_quit",
                        text="Quit",
                        font=self.files.get_font(30),
                        text_color=(255, 255, 255),
                        img_file_str=self.files.get_button_img_str(),
                        b_color=b_color,
                        position=(self.screen_size[0] // 2 - b_size[0] // 2,
                                  self.screen_size[1] // 1.4),
                        size=b_size,
                        rotate=0)

        self.buttons.add(b_play)
        self.buttons.add(b_scores)
        self.buttons.add(b_quit)

        self.all_sprites.add(self.buttons)
    
    def update_pop_ups(self, tag: str, b_press=set()):
        """Renderöi pop-up ikkunat näkyville tagin perusteella. Myös sen napit.

        Args:
            tag (str): mikä pop-up ikkuna halutaan näkyville.
            b_press (set(str), valinnainen): Renderöi kaikki setissä olevat napit painetuiksi.
        """
        size = (450, 350)
        x = (self.screen_size[0] - size[0]) // 2
        y = (self.screen_size[1] - size[1]) // 2
        restart_pop = Tile(0, x, y, color=(100, 100, 100))
        restart_pop.color = (230, 200, 200)
        restart_pop.image = pg.transform.scale(restart_pop.img, size)
        self.pop_ups.add(restart_pop)

        # Buttons:

        margin = 15
        b_size = (180, 35)
        if "b_4x4" in b_press:
            b_color = (0, 100, 0)
        else:
            b_color = (0, 200, 0)
        b_4x4 = Button(tag="b_4x4",
                       text="4x4",
                       text_color=(240, 240, 240),
                       font=self.files.get_font(33),
                       img_file_str=self.files.get_button_img_str(),
                       b_color=b_color,
                       position=(self.screen_size[0] // 2 - b_size[0] // 2,
                                 self.screen_size[1] // 2.5),
                       size=b_size,
                       rotate=0)
        
        if "b_5x5" in b_press:
            b_color = (0, 100, 0)
        else:
            b_color = (0, 200, 0)
        b_5x5 = Button(tag="b_5x5",
                       text="5x5",
                       text_color=(240, 240, 240),
                       font=self.files.get_font(33),
                       img_file_str=self.files.get_button_img_str(),
                       b_color=b_color,
                       position=(self.screen_size[0] // 2 - b_size[0] // 2,
                                 self.screen_size[1] // 2),
                       size=b_size,
                       rotate=0)
        
        if "b_6x6" in b_press:
            b_color = (0, 100, 0)
        else:
            b_color = (0, 200, 0)
        b_6x6 = Button(tag="b_6x6",
                       text="6x6",
                       text_color=(240, 240, 240),
                       font=self.files.get_font(33),
                       img_file_str=self.files.get_button_img_str(),
                       b_color=b_color,
                       position=(self.screen_size[0] // 2 - b_size[0] // 2,
                                 self.screen_size[1] // 1.666),
                       size=b_size,
                       rotate=0)

        b_size = (120, 35)
        if "b_back" in b_press:
            b_color = (100, 0, 0)
        else:
            b_color = (200, 0, 0)
        b_back = Button(tag="b_back",
                      text="Back",
                      text_color=(240, 240, 240),
                      img_file_str=self.files.get_button_img_str(),
                      b_color=b_color,
                      position=(self.screen_size[0] // 2 - b_size[0] // 2,
                                self.screen_size[1] // 1.4),
                      size=b_size,
                      rotate=0)

        self.pop_up_buttons.add(b_4x4)
        self.pop_up_buttons.add(b_5x5)
        self.pop_up_buttons.add(b_6x6)
        self.pop_up_buttons.add(b_back)

        # Text:
        x = x + margin
        y = y + margin
        s = ""
        if tag == "play":
            s = "Choose size of grid:"
        text = Text(s,
                    x, y, 40, (255, 255, 255),
                    size[0] - margin * 2, 80, (100, 100, 100))

        self.pop_ups.add(text)
