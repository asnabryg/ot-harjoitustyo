
import pygame as pg
import os

dirname = os.path.dirname(__file__)

class Button(pg.sprite.Sprite):
    """Luokka, jolla luodaan nappi.
    """

    def __init__(self, tag: str, text=None, text_color=(255, 255, 255), img_file_str="button.png", b_color=(0, 0, 0), position=(0, 0), size=(80, 80), rotate=0):
        """Luokan konstruktori, joka luo uuden napin.

        Args:
            tag (str): Napin tag, jotta nappi voidaan tunnistaa,
            text (str, valinnainen): Napin teksti. Oletus None,
            text_color (tuple, valinnainen): Napin tekstin väri. Oletus (255, 255, 255)
            img_file (str, valinnainen): Napin kuva. Oletus "button.png",
            b_color (tuple): Napin väri. Oletus (0, 0, 0),
            position (tuple): Napin positio näytöllä,
            size (tuple): Napin leveys ja korkeus. Oletus (50, 50).
            rotate (int): Napin kiertokulma. Oletus 0.
            files (GameFiles()): Pelin kaikki avatut tiedostot
        """

        super().__init__()
        self.tag = tag

        self.img = pg.image.fromstring(img_file_str, (128, 128), "RGBA")
        
        self.img.fill(b_color, None, pg.BLEND_RGB_MULT)
        
        self.rect = self.img.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.rect.w = size[0]
        self.rect.h = size[1]
        self.image = pg.transform.rotate(self.img, rotate)
        self.image = pg.transform.scale(self.image, size)

        if text is not None:
            self.font = pg.font.SysFont("default", 30)
            self.text = self.font.render(text, 1, text_color)
        
            R, G, B = b_color[0] - 60, b_color[1] - 60, b_color[2] - 60
            R = 0 if R < 0 else R
            G = 0 if G < 0 else G
            B = 0 if B < 0 else B
            self.text_outline = self.font.render(text, 1, (R, G, B))

            text_x = size[0] // 2 - self.text.get_width() // 2
            text_y = (size[1] // 2 - self.text.get_height() // 2) + 2
            self.image.blit(self.text_outline, (text_x+1, text_y+1))
            self.image.blit(self.text_outline, (text_x-1, text_y-1))
            self.image.blit(self.text_outline, (text_x+1, text_y-1))
            self.image.blit(self.text_outline, (text_x-1, text_y+1))
            self.image.blit(self.text, (text_x, text_y))
