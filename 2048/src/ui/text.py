
import pygame as pg


class Text(pg.sprite.Sprite):
    """Luokka, jolla alustetaan teksti ruudulle.
    Luokka perii pygamesta sprite luokan.
    """

    def __init__(self, text: str, x, y, size: int, text_color: tuple, width, height, back_color, outline="thin", outline_style="full"):
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
        self.font = pg.font.SysFont("default", size)
        self.textSurf = self.font.render(text, 1, text_color)
        if back_color is not None:
            R, G, B = back_color[0] - 60, back_color[1] - 60, back_color[2] - 60
            R = 0 if R < 0 else R
            G = 0 if G < 0 else G
            B = 0 if B < 0 else B
        else:
            R, G, B = 20, 20, 20
        self.text_outline = self.font.render(text, 1, (R, G, B))
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if back_color is not None:
            self.image.fill(back_color)
        W = width/2 - self.textSurf.get_width()/2
        H = height/2 - self.textSurf.get_height()/2
        if outline_style is not None:
            if outline == "thin":
                increase = 1
            elif outline == "fat":
                increase = 5
            if outline_style == "full" or outline_style == "shadow":
                self.image.blit(self.text_outline, (W+increase, H+increase))
            if outline_style == "full":
                self.image.blit(self.text_outline, (W-increase, H-increase))
                self.image.blit(self.text_outline, (W+increase, H-increase))
                self.image.blit(self.text_outline, (W-increase, H+increase))
        self.image.blit(self.textSurf, [W, H])
