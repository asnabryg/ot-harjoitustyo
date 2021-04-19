
import unittest
from game2048 import Game2048


class TestGame(unittest.TestCase):

    def setUp(self):
        seed = 0
        self.game = Game2048(4, r_seed=seed)
        self.game_full = Game2048(4, board=[[2, 4, 8, 16],
                                            [4, 2, 16, 8],
                                            [2, 4, 8, 16],
                                            [4, 2, 16, 8]])
        self.game_test1 = Game2048(4, board=[[2, 4, 8, 16],
                                             [4, 2, 2, 8],
                                             [2, 4, 8, 16],
                                             [4, 2, 16, 8]])
        self.game_test2 = Game2048(4, board=[[2, 4, 8, 32],
                                             [4, 2, 16, 32],
                                             [2, 4, 8, 16],
                                             [4, 2, 16, 8]])
        self.game_test_horizontal = Game2048(4, board=[[2, 4, 4, 2],
                                                       [0, 0, 2, 0],
                                                       [2, 2, 0, 2],
                                                       [2, 2, 2, 2]], r_seed=seed)
        self.game_test_vertical = Game2048(4, board=[[2, 0, 2, 2],
                                                     [4, 0, 2, 2],
                                                     [4, 2, 0, 2],
                                                     [2, 0, 2, 2]], r_seed=seed)

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
        bool = self.game_full.add_new_tile()
        print(self.game_full.get_board())
        self.assertEqual(bool, False)

    def test_game_over(self):
        bool = self.game_full.check_if_gameover()
        self.assertEqual(bool, True)
        bool = self.game_test1.check_if_gameover()
        self.assertEqual(bool, False)
        bool = self.game_test2.check_if_gameover()
        self.assertEqual(bool, False)
        bool = self.game.check_if_gameover()
        self.assertEqual(bool, False)

    def test_move_left(self):
        self.game_test_horizontal.move_left()
        model_solution = [[2, 8, 2, 0],
                          [2, 0, 0, 0],
                          [4, 2, 0, 0],
                          [4, 4, 2, 0]]
        self.assertEqual(self.game_test_horizontal.get_board(), model_solution)
        self.game_full.move_left()
        model_solution = [[2, 4, 8, 16],
                          [4, 2, 16, 8],
                          [2, 4, 8, 16],
                          [4, 2, 16, 8]]
        self.assertEqual(self.game_full.get_board(), model_solution)

    def test_move_right(self):
        self.game_test_horizontal.move_right()
        model_solution = [[0, 2, 8, 2],
                          [0, 0, 0, 2],
                          [0, 0, 2, 4],
                          [2, 0, 4, 4]]
        self.assertEqual(self.game_test_horizontal.get_board(), model_solution)
        self.game_full.move_right()
        model_solution = [[2, 4, 8, 16],
                          [4, 2, 16, 8],
                          [2, 4, 8, 16],
                          [4, 2, 16, 8]]
        self.assertEqual(self.game_full.get_board(), model_solution)

    def test_move_up(self):
        self.game_test_vertical.move_up()
        model_solution = [[2, 2, 4, 4],
                          [8, 0, 2, 4],
                          [2, 0, 0, 0],
                          [0, 0, 2, 0]]
        self.assertEqual(self.game_test_vertical.get_board(), model_solution)
        self.game_full.move_up()
        model_solution = [[2, 4, 8, 16],
                          [4, 2, 16, 8],
                          [2, 4, 8, 16],
                          [4, 2, 16, 8]]
        self.assertEqual(self.game_full.get_board(), model_solution)

    def test_move_down(self):
        self.game_test_vertical.move_down()
        model_solution = [[0, 0, 0, 0],
                          [2, 0, 0, 2],
                          [8, 0, 2, 4],
                          [2, 2, 4, 4]]
        self.assertEqual(self.game_test_vertical.get_board(), model_solution)
        self.game_full.move_down()
        model_solution = [[2, 4, 8, 16],
                          [4, 2, 16, 8],
                          [2, 4, 8, 16],
                          [4, 2, 16, 8]]
        self.assertEqual(self.game_full.get_board(), model_solution)
