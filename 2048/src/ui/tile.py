
import pygame as pg
import os

dirname = os.path.dirname(__file__)

class Tile(pg.sprite.Sprite):
    """Luokka, jossa on pelilaatan kaikki tiedot. (arvo, xy -koordinaatti, kuva).
    Luokka perii pygamesta sprite luokan.
    """

    def __init__(self, tile_value=0, x=0, y=0, cell_size=80):
        """Luokan konstruktori, joka luo uuden laatan ja antaa arvon ja xy -koordinaatti
        positioni siihen.
        Jos arvo on 0, laatta on taustalaatta.
        Laatan väri muuttuu arvon mukaan.

        Args:
            tile_value (int): Laatan arvo,
            x (int): x arvo,
            y (int): y arvo,
            cell_size (int): cell width and heigth size

        """

        super().__init__()
        self.value = tile_value

        file = "tile.png" if tile_value > 0 else "tile0.png"
        self.img = pg.image.load(os.path.join(dirname, "./../assets", file)).convert_alpha()

        self.color = (0, 0, 0)
        if tile_value > 0:
            if tile_value == 2:
                self.color = (238, 227, 222)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 4:
                self.color = (231, 223, 198)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 8:
                self.color = (247, 178, 123)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 16:
                self.color=(239, 146, 99)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 32:
                self.color = (247, 123, 95)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 64:
                self.color = (234, 90, 56)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 128:
                self.color = (239, 206, 115)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 256:
                self.color = (242, 208, 75)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 512:
                self.color = (238, 198, 82)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 1024:
                self.color = (239, 194, 66)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 2048:
                self.color = (236, 187, 2)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 4096:
                self.color = (96, 182, 146)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 8192:
                self.color = (96, 198, 255)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 16384:
                self.color = (96, 162, 255)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 32768:
                self.color = (96, 123, 255)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 65536:
                self.color = (96, 80, 255)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 131072:
                self.color = (96, 40, 255)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 131072:
                self.color = (96, 0, 255)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 262144:
                self.color = (96, 0, 200)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 524288:
                self.color = (96, 0, 160)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 1048576:
                self.color = (96, 0, 130)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 2097152:
                self.color = (96, 0, 85)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            elif tile_value == 4194304:
                self.color = (96, 0, 40)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)
            else:
                self.color = (80, 0, 0)
                self.img.fill(self.color, None, pg.BLEND_RGBA_MULT)

        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = pg.transform.scale(self.img, (cell_size, cell_size))

        if tile_value > 0:
            div = 5
            div2 = 2
            size = 33
            if tile_value > 9:
                div = 4
            if tile_value > 99:
                div = 3
            if tile_value > 999:
                div = 3
            if tile_value > 9999:
                div = 2.8
            if tile_value > 99999:
                div = 2.7
                size = 28
            if tile_value > 999999:
                div = 2.7
                div2 = 1.8
                size = 24
            if tile_value > 9999999:
                div = 2.7
                div2 = 1.75
                size = 21
            if tile_value > 99999999:
                div = 2.7
                div2 = 1.75
                size = 20
            if tile_value > 999999999:
                div = 2.7
                div2 = 1.75
                size = 20
            

            self.font = pg.font.SysFont("default", size)
            self.text = self.font.render(str(tile_value), 1, (255, 255, 255))

            R, G, B = self.color[0] - 60, self.color[1] - 60, self.color[2] - 60
            R = 0 if R < 0 else R
            G = 0 if G < 0 else G
            B = 0 if B < 0 else B
            self.text_outline = self.font.render(
                str(tile_value), 1, (R, G, B))

            text_x = self.img.get_width() // 2 if div == 5 else self.img.get_width() // 2 - self.text.get_width() // div
            text_y = self.img.get_height() // div2
            self.image.blit(self.text_outline, (text_x+1, text_y+1))
            self.image.blit(self.text_outline, (text_x-1, text_y-1))
            self.image.blit(self.text_outline, (text_x+1, text_y-1))
            self.image.blit(self.text_outline, (text_x-1, text_y+1))
            self.image.blit(self.text, (text_x, text_y))
