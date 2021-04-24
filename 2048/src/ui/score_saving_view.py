
import pygame as pg
from ui.tile import Tile
from ui.text import Text
from ui.button  import Button

class ScoreSavingView():

    def __init__(self, files, screen_size: tuple, score):
        self.buttons = pg.sprite.Group()
        self.texts = pg.sprite.Group()
        self.name_surface = pg.sprite.Group()
        self.name = ""
        self.score = score
        self.pop_ups = pg.sprite.Group()
        self.files = files
        self.screen_size = screen_size
        self.surface_size = ()
        self.initialize()

    def initialize(self):
        self.surface_size = (int(self.screen_size[0] * 0.7), int(self.screen_size[1] * 0.7))
        if self.surface_size[0] > 546 or self.surface_size[1] > 336:
            self.surface_size = (546, 336)
        xy_position = (self.screen_size[0] // 2 - self.surface_size[0] //
                       2, self.screen_size[1] // 2 - self.surface_size[1] // 2)
        surface = Tile(0, xy_position[0], xy_position[1],
                            image=self.files.get_tile0_img_str(), files=self.files,
                            color=(100, 100, 100))
        surface.image = pg.transform.scale(surface.img, self.surface_size)
        self.pop_ups.add(surface)

        #Texts
        margin = 15
        x = xy_position[0] + margin
        y = xy_position[1] + margin
        gameover = Text("Gameover!", x, y, 40, (255, 255, 255),
                    self.surface_size[0] - margin * 2, 60, (100, 100, 100))
        
        x = xy_position[0] + margin
        y = y = xy_position[1] + margin + 60 + margin
        score = Text("Your score:" + str(self.score), x, y, 33, (255, 255, 255),
                    self.surface_size[0] - margin * 2, 40, (61, 61, 60))

        x = xy_position[0] + margin
        y = self.screen_size[1] // 1.6 - 40 // 2 - 50
        text = Text("Choose nickname:", x, y, 33, (255, 255, 255),
                    self.surface_size[0] - margin * 2, 40, (61, 61, 60))
        
        self.texts.add(gameover)
        self.texts.add(score)
        self.texts.add(text)

    def update_buttons(self, b_press=set()):
        self.buttons = pg.sprite.Group()
        b_size = (120, 35)
        if "b_submit" in b_press:
            b_color = (0, 100, 0)
        else:
            b_color = (0, 200, 0)
        b_submit = Button(tag="b_submit",
                        text="Submit",
                        text_color=(240, 240, 240),
                        img_file_str=self.files.get_button_img_str(),
                        b_color=b_color,
                        position=(self.screen_size[0] // 2 - b_size[0] // 2,
                                  self.screen_size[1] // 1.6 + 40),
                        size=b_size,
                        rotate=0)
        self.buttons.add(b_submit)

    def update_name(self, char="", backspace=False):
        self.name_surface = pg.sprite.Group()
        self.name = self.name + char
        if backspace:
            self.name = self.name[:-1]
        x = self.screen_size[0] // 2 - 250 // 2
        y = self.screen_size[1] // 1.6 - 40 // 2
        text = Text(self.name, x, y, 33, (0, 0, 0),
                    250, 40, (255, 255, 255))

        self.name_surface.add(text)
