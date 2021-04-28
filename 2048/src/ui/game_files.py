
import os
import pygame as pg

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)


class GameFiles():
    """Luokka, joka avaa valmiiksi kaikki kuvatiedostot ja hakee fontit, jotta peli ei turhaan avaa samaa tiedostoa monta kertaa.
    Luokka muuntaa kuvat string muotoon, jolloin kuvan kopioiminen on helppoa uudeksi kuvaksi.
    """

    def __init__(self):
        """Luokan konstruktori, joka hakee/avaa kuvat ja fontit valmiiksi.
        """
        asset_path = "./../assets"
        self.__tile0 = pg.image.load(
            os.path.join(dirname, asset_path, "tile0.png"))
        self.__tile0 = pg.image.tostring(self.__tile0, "RGBA")
        self.__tile = pg.image.load(os.path.join(
            dirname, asset_path, "tile.png"))
        self.__tile = pg.image.tostring(self.__tile, "RGBA")
        self.__button = pg.image.load(
            os.path.join(dirname, asset_path, "button.png"))
        self.__button = pg.image.tostring(self.__button, "RGBA")
        self.__button_up = pg.image.load(
            os.path.join(dirname, asset_path, "button_up.png"))
        self.__button_up = pg.image.tostring(self.__button_up, "RGBA")

        font = "default"
        self.font40 = pg.font.SysFont(font, 40)
        self.font33 = pg.font.SysFont(font, 33)
        self.font28 = pg.font.SysFont(font, 28)
        self.font24 = pg.font.SysFont(font, 24)
        self.font21 = pg.font.SysFont(font, 21)
        self.font20 = pg.font.SysFont(font, 20)

    def get_tile_img_str(self):
        """Palauttaa laatan kuvatiedoston stringinä.

        Returns:
            str: kuvatiedosto
        """
        return self.__tile

    def get_tile0_img_str(self):
        """Palauttaa taustalaatan kuvatiedoston stringinä.

        Returns:
            str: kuvatiedosto
        """
        return self.__tile0

    def get_button_img_str(self):
        """Palauttaa napin kuvatiedoston stringinä.

        Returns:
            str: kuvatiedosto
        """
        return self.__button

    def get_button_up_img_str(self):
        """Palauttaa nuoli napin kuvatiedoston stringinä. Nuoli osoittaa ylös päin.

        Returns:
            str: kuvatiedosto
        """
        return self.__button_up

    def get_font(self, size):
        """Palauttaa fontti tyypin tietyllä koolla.
        Mahdolliset koot 20, 21, 24, 28, 33 ja 40.

        Args:
            size (int): fontin koko

        Returns:
            pygame.font: fontti
        """
        font = None
        if size == 33:
            font = self.font33
        elif size == 28:
            font = self.font28
        elif size == 24:
            font = self.font24
        elif size == 21:
            font = self.font21
        elif size == 20:
            font = self.font20
        elif size == 40:
            font = self.font40
        return font
