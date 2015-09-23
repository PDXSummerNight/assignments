import unittest
from game import Board

# python -m unittest

class IsBoardFullTest(unittest.TestCase):
    # game is list of lists
    # 0 is empty
    # 1 is player 1
    # 2 is player 2

    def setUp(self):
        self.board = Board()

    def tearDown(self):
        del self.board

    def test_is_board_full_full(self):
        matrix = [[1, 1, 2, 2], [2, 1, 2, 1]]
        is_full = self.board.is_board_full(matrix)

        self.assertTrue(is_full, "Full board check returned not full")

    def test_is_board_full_empty(self):
        pass

    def test_is_board_full_midgame(self):
        pass
