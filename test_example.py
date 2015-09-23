import unittest
from game import Connect4Game

class Connect4WinnerTest(unittest.TestCase):

   def setUp(self):
      self.game = Connect4Game()
      self.game.player1 = Player("nancy")
      self.game.player2 = Player("levin")

   def tearDown(self):
      del self.game

   def test_winner_check_horizontal_win(self):
      """Test that when a valid Horizontal winning board is passed, the win is confirmed."""
      winningList = [['o','o','o','o']]

      didWin = self.game.check_winner(winningList)

      self.assertTrue(didWin, "Horizontal win condition was not found")


   def test_swap_players_levin(self):

      #SOME CODE

      self.assertEqual(playerIGotBack.name, "levin", "Did not get Levin back :(")