
import unittest
from game2048 import Game2048


class TestGame(unittest.TestCase):

    def setUp(self):
        seed = 0
        self.game = Game2048(4, seed)
        self.game_full = Game2048(4, seed)

    def test_new_empty_board_exists_4x4(self):
        board = self.game.get_board()
        n = self.game.get_size()
        row = [0] * n
        for x in board:
            self.assertEqual(x, row)

    def test_get_random_empty_place(self):
        empty_place = self.game.get_random_empty_place()
        self.assertEqual(empty_place, (3, 0))

    def test_add_new_tile_for_empty_board(self):
        bool = self.game.add_new_tile()
        board = self.game.get_board()
        self.assertEqual(board[3][0], 2)
        self.assertEqual(bool, True)

    def test_add_new_tile_for_full_board(self):
        n = self.game_full.get_size()
        for _ in range(n*n):
            self.game_full.add_new_tile()
            print(self.game_full.get_board())
        bool = self.game_full.add_new_tile()
        print(self.game_full.get_board())
        self.assertEqual(bool, False)
