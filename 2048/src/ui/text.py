
import pygame as pg
from pygame.constants import BLEND_RGB_MULT

class Text(pg.sprite.Sprite):
    """Luokka, jolla alustetaan teksti ruudulle.
    Luokka perii pygamesta sprite luokan.
    """

    def __init__(self, text: str, x, y, size: int, text_color: tuple, width, height, back_color):
        """Luokan konstruktori, joka luo uuden teksti spriten.

        Args:
            text (str): teksti,
            x (int): x koordinaatti
            y (int): y koordinaatti
            size (int): fontin koko
            text_color (tuple): tekstin väri
            width (int): spriten leveys
            height (int): spriten korkeus
            back_color (tuple): tausta spriten väri
        """

        super().__init__()
        self.font = pg.font.SysFont("Comic Sans", size)
        self.textSurf = self.font.render(text, 1, text_color)
        self.image = pg.Surface((width, height))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(back_color)
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
