
import pygame as pg
import os

dirname = os.path.dirname(__file__)

class Tile(pg.sprite.Sprite):
    """Luokka, jossa on pelilaatan kaikki tiedot. (arvo, xy -koordinaatti, kuva).
    Luokka perii pygamesta sprite luokan.
    """

    def __init__(self, tile_value=0, x=0, y=0):
        """Luokan konstruktori, joka luo uuden laatan ja antaa arvon ja xy -koordinaatti
        positioni siihen.
        Jos arvo on 0, laatta on taustalaatta.
        Laatan väri muuttuu arvon mukaan.

        Args:
            tile_value (int): Laatan arvo
            x (int): x arvo
            y (int): y arvo
        """

        super().__init__()
        self.value = tile_value

        file = "tile.png" if tile_value > 0 else "tile0.png"
        self.img = pg.image.load(os.path.join(dirname, "assets", file)).convert_alpha()

        if tile_value == 2:
            self.img.fill((238, 227, 222), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 4:
            self.img.fill((231, 223, 198), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 8:
            self.img.fill((247, 178, 123), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 16:
            self.img.fill((239, 146, 99), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 32:
            self.img.fill((247, 123, 95), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 64:
            self.img.fill((234, 90, 56), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 128:
            self.img.fill((239, 206, 115), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 256:
            self.img.fill((242, 208, 75), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 512:
            self.img.fill((238, 198, 82), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 1024:
            self.img.fill((239, 194, 66), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 2048:
            self.img.fill((236, 187, 2), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 4096:
            self.img.fill((236, 187, 2), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 8192:
            self.img.fill((96, 198, 255), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 16384:
            self.img.fill((96, 162, 255), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 32768:
            self.img.fill((96, 123, 255), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 65536:
            self.img.fill((96, 80, 255), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 131072:
            self.img.fill((96, 40, 255), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 131072:
            self.img.fill((96, 0, 255), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 262144:
            self.img.fill((96, 0, 200), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 524288:
            self.img.fill((96, 0, 160), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 1048576:
            self.img.fill((96, 0, 130), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 2097152:
            self.img.fill((96, 0, 85), None, pg.BLEND_RGBA_MULT)
        elif tile_value == 4194304:
            self.img.fill((96, 0, 40), None, pg.BLEND_RGBA_MULT)
        elif tile_value > 0:
            self.img.fill((80, 0, 0), None, pg.BLEND_RGBA_MULT)

        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = pg.transform.scale(self.img, (80, 80))
