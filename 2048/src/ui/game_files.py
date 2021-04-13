
import os
import pygame as pg

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)

class GameFiles():

    def __init__(self):
        asset_path = "./../assets"
        self.__tile0 = pg.image.load(
            os.path.join(dirname, asset_path, "tile0.png"))
        self.__tile0 = pg.image.tostring(self.__tile0, "RGBA")
        self.__tile = pg.image.load(os.path.join(
            dirname, asset_path, "tile.png"))
        self.__tile = pg.image.tostring(self.__tile, "RGBA")

        self.font33 = pg.font.SysFont("default", 33)
        self.font28 = pg.font.SysFont("default", 28)
        self.font24 = pg.font.SysFont("default", 24)
        self.font21 = pg.font.SysFont("default", 21)
        self.font20 = pg.font.SysFont("default", 20)
    
    def get_tile(self):
        return self.__tile
    
    def get_tile0(self):
        return self.__tile0
    
    def get_font(self, size):
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
        return font
