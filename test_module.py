# test_module.py
import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

class RPS_Test(unittest.TestCase):
    def test_quincy(self):
        result = play(player, quincy, 1000)
        self.assertGreater(result["Player 1"], 600)

    def test_abbey(self):
        result = play(player, abbey, 1000)
        self.assertGreater(result["Player 1"], 600)

    def test_kris(self):
        result = play(player, kris, 1000)
        self.assertGreater(result["Player 1"], 600)

    def test_mrugesh(self):
        result = play(player, mrugesh, 1000)
        self.assertGreater(result["Player 1"], 600)

if __name__ == "__main__":
    unittest.main()
