
import pygame as pg
from tile import Tile
from game2048 import Game2048

class GameView():

    def __init__(self, game: Game2048):
        self.game = game
        self.tiles = pg.sprite.Group()
        self.cell_size = 80
        self.all_sprites = pg.sprite.Group()
        self.initialize()

    def initialize(self):
        board = self.game.get_board()
        size = self.game.get_size()

        for y in range(size):
            for x in range(size):
                cell = board[y][x]
                normalized_x = x * self.cell_size + (320//4)
                normalized_y = y * self.cell_size + (240//2)
                
                self.tiles.add(Tile(0, normalized_x, normalized_y))  # tausta
                if cell == 0:
                    continue
                self.tiles.add(Tile(cell, normalized_x, normalized_y))  # tile

        self.all_sprites.add(self.tiles)
