
import pygame as pg
from ui.tile import Tile
from ui.text import Text
from game2048 import Game2048

class GameView():

    def __init__(self, game: Game2048, cell_size):
        self.game = game
        self.tiles = pg.sprite.Group()
        self.texts = pg.sprite.Group()
        self.cell_size = cell_size
        self.all_sprites = pg.sprite.Group()
        self.initialize()

    def initialize(self):
        board = self.game.get_board()
        size = self.game.get_size()

        score = self.game.get_score()
        text = "Score: " + str(score)
        margin = 15
        score_x = (310//6) + margin
        score_y = (240//2) - (self.cell_size - margin)
        self.texts.add(Text(text, score_x, score_y, 35, (255, 255, 255), self.cell_size*self.game.get_size() - margin*2, 50, (0, 0, 180)))

        for y in range(size):
            for x in range(size):
                cell = board[y][x]
                normalized_x = x * self.cell_size + (310//6)
                normalized_y = y * self.cell_size + (240//2)

                self.tiles.add(Tile(0, normalized_x, normalized_y, self.cell_size))  # tausta
                if cell == 0:
                    continue
                self.tiles.add(Tile(cell, normalized_x, normalized_y, self.cell_size))  # tile

        self.all_sprites.add(self.tiles, self.texts)
