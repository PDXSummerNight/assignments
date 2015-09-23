import unittest
import game from connect4

class Connect4Winner(unittest.TestCase):

    def test_winner_check_horizontal_win(self):
        winningList = [['o', 'o', 'o']]
        didWin = self.game
        #override setup and teardown
    def setUp(self):
        self.game = Connect4Game()

    def tearDown(self):
        del self.game

        self.assertEqual(min, max, "Horizontal win condition was not found")
