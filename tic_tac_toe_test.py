import unittest
from crestiki_noliki import Game


class TestGame(unittest.TestCase):

    def test_1(self):
        game_1 = Game()
        game_1.set_sign(1, "x")
        game_1.set_sign(2, "o")
        game_1.set_sign(3, "x")
        game_1.set_sign(4, "o")
        self.assertEqual(game_1.check_win_condition(), False)
        game_1.set_sign(5, "x")
        game_1.set_sign(6, "o")
        game_1.set_sign(8, "x")
        game_1.set_sign(7, "o")
        self.assertEqual(game_1.check_win_condition(), False)
        game_1.set_sign(9, "x")
        self.assertEqual(game_1.check_win_condition(), True)

    def test_2(self):
        game_2 = Game()
        game_2.set_sign(1, "o")
        game_2.set_sign(2, "o")
        game_2.set_sign(3, "o")
        self.assertEqual(game_2.check_win_condition(), True)

    def test_3(self):
        game_3 = Game()
        game_3.set_sign(1, "x")
        game_3.set_sign(2, "o")
        game_3.set_sign(3, "o")
        # game_3.display()
        self.assertEqual(game_3.check_win_condition(), False)
        game_3.set_sign(4, "o")
        game_3.set_sign(5, "x")
        game_3.set_sign(6, "x")
        self.assertEqual(game_3.check_win_condition(), False)
        game_3.set_sign(7, "o")
        game_3.set_sign(8, "x")
        game_3.set_sign(9, "o")
        self.assertEqual(game_3.check_win_condition(), False)


if __name__ == "__main__":
    unittest.main()
