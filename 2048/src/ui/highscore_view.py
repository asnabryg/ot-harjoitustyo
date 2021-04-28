
import pygame as pg
from repositories.score_repository import ScoreRepository
from ui.button import Button
from ui.text import Text
from ui.game_files import GameFiles

class HighscoreView:

    def __init__(self, screen_size:int, repository: ScoreRepository, files: GameFiles, score_list, buttons_down=set()):
        self.buttons = pg.sprite.Group()
        self.score_list = score_list
        self.texts = pg.sprite.Group()
        self.rep = repository
        self.files = files
        self.screen_size = screen_size
        self.all_sprites = pg.sprite.Group()
        self.btns_down = buttons_down
        self.initialize()
    
    def initialize(self):
        print(self.score_list)
        surface_size = (300, 60)
        self.texts.add(Text(text="Highscores",
                            x=self.screen_size[0] // 2 - surface_size[0] // 2,
                            y=10,
                            size=60,
                            text_color=(255, 255, 255),
                            width=surface_size[0],
                            height=surface_size[1],
                            back_color=(0, 0, 200),
                            outline="fat",
                            outline_style="shadow"))
        
        margin = 10
        pos_x = 15
        pos_y = 200
        surface_size = (400, 40)
        top_n = 1
        if len(self.score_list) > 0:
            # nicknames
            self.texts.add(Text(text="Nicknames:",
                                x=pos_x + 40 + margin,
                                y=pos_y - surface_size[1] - margin,
                                size=40,
                                text_color=(255, 255, 255),
                                width=surface_size[0],
                                height=surface_size[1],
                                back_color=(0, 0, 120),
                                outline="thin",
                                outline_style="outline",
                                text_position="left"))
            # scores
            self.texts.add(Text(text="Scores:",
                                x=pos_x + 40 + margin * 2 + surface_size[0],
                                y=pos_y - surface_size[1] - margin,
                                size=40,
                                text_color=(255, 255, 255),
                                width=225,
                                height=surface_size[1],
                                back_color=(0, 0, 120),
                                outline="thin",
                                outline_style="outline",
                                text_position="left"))

            for player in self.score_list:
                # top position (1-5)
                self.texts.add(Text(text=str(top_n),
                                    x=pos_x,
                                    y=pos_y,
                                    size=45,
                                    text_color=(255, 255, 255),
                                    width=40,
                                    height=surface_size[1],
                                    back_color=(0, 0, 120),
                                    outline="thin",
                                    outline_style="outline"))
                # name
                self.texts.add(Text(text=str(player[0]),
                                    x=pos_x + 40 + margin,
                                    y=pos_y,
                                    size=45,
                                    text_color=(255, 255, 255),
                                    width=surface_size[0],
                                    height=surface_size[1],
                                    back_color=(0, 0, 150),
                                    outline="thin",
                                    outline_style="outline",
                                    text_position="left"))
                # score
                self.texts.add(Text(text=str(player[1]),
                                    x=pos_x + 40 + margin * 2 + surface_size[0],
                                    y=pos_y,
                                    size=45,
                                    text_color=(255, 255, 255),
                                    width=225,
                                    height=surface_size[1],
                                    back_color=(0, 0, 150),
                                    outline="thin",
                                    outline_style="outline",
                                    text_position="right"))
                pos_y += surface_size[1] + margin
                top_n += 1
        else:
            # no highscores yet
            surface_size = (300, 60)
            self.texts.add(Text(text="No highscores yet!",
                                x=self.screen_size[0] // 2 - surface_size[0] // 2,
                                y=self.screen_size[0] // 2 - surface_size[0] // 2,
                                size=40,
                                text_color=(255, 255, 255),
                                width=surface_size[0],
                                height=surface_size[1],
                                back_color=(0, 0, 150),
                                outline="thin",
                                outline_style="outline"))
        
        self.update_buttons()
        self.all_sprites.add(self.texts)
    
    def update_buttons(self, b_press=set()):
        self.all_sprites.remove(self.buttons)
        if b_press == set():
            b_press = self.btns_down
        
        margin = 15
        b_size = (75, 30)
        b_press_up_color = (200, 0, 0)
        b_press_down_color = (100, 0, 0)
        if "b_back" in b_press:
            b_color = b_press_down_color
        else:
            b_color = b_press_up_color
        b_back = Button(tag="b_back",
                        text="Back",
                        font=self.files.get_font(33),
                        text_color=(255, 255, 255),
                        img_file_str=self.files.get_button_img_str(),
                        b_color=b_color,
                        position=(margin, margin),
                        size=b_size,
                        rotate=0)
        
        b_size = (75, 30)
        c = (self.screen_size[0] // 2 - b_size[0] // 2) - b_size[0] -margin
        y_pos = b_size[1] + margin * 3
        b_press_up_color = (0, 200, 0)
        b_press_down_color = (0, 100, 0)
        if "b_4x4" in b_press:
            b_color = b_press_down_color
        else:
            b_color = b_press_up_color
        b_4x4 = Button(tag="b_4x4",
                        text="4x4",
                        font=self.files.get_font(33),
                        text_color=(255, 255, 255),
                        img_file_str=self.files.get_button_img_str(),
                        b_color=b_color,
                        position=(c, y_pos),
                        size=b_size,
                        rotate=0)
        b_press_up_color = (0, 200, 0)
        b_press_down_color = (0, 100, 0)
        if "b_5x5" in b_press:
            b_color = b_press_down_color
        else:
            b_color = b_press_up_color
        b_5x5 = Button(tag="b_5x5",
                       text="5x5",
                       font=self.files.get_font(33),
                       text_color=(255, 255, 255),
                       img_file_str=self.files.get_button_img_str(),
                       b_color=b_color,
                       position=(c + b_size[0] + margin, y_pos),
                       size=b_size,
                       rotate=0)
        b_press_up_color = (0, 200, 0)
        b_press_down_color = (0, 100, 0)
        if "b_6x6" in b_press:
            b_color = b_press_down_color
        else:
            b_color = b_press_up_color
        b_6x6 = Button(tag="b_6x6",
                       text="6x6",
                       font=self.files.get_font(33),
                       text_color=(255, 255, 255),
                       img_file_str=self.files.get_button_img_str(),
                       b_color=b_color,
                       position=(c + b_size[0] * 2 + margin * 2, y_pos),
                       size=b_size,
                       rotate=0)
        
        self.buttons.add(b_back)
        self.buttons.add(b_4x4)
        self.buttons.add(b_5x5)
        self.buttons.add(b_6x6)

        self.all_sprites.add(self.buttons)

