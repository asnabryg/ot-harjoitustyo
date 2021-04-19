
from typing import Text
import pygame as pg
from ui.button import Button
from ui.text import Text


class MenuView:

    def __init__(self, screen_size, files):
        self.buttons = pg.sprite.Group()
        self.texts = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.screen_size = screen_size
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
