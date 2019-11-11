import unittest
from crestiki_noliki import Game


class TestGame(unittest.TestCase):

    def test_order_type_game(self):
        game_1 = Game()
        game_1.set_sign(1, "x")
        game_1.set_sign(2, "o")
        game_1.set_sign(3, "x")
        game_1.set_sign(4, "o")
        self.assertFalse(game_1.check_win_condition())
        game_1.set_sign(5, "x")
        game_1.set_sign(6, "o")
        game_1.set_sign(8, "x")
        game_1.set_sign(7, "o")
        self.assertFalse(game_1.check_win_condition())
        game_1.set_sign(9, "x")
        self.assertTrue(game_1.check_win_condition())

    def test_in_line_combination(self):
        game_2 = Game()
        game_2.set_sign(1, "o")
        game_2.set_sign(2, "o")
        game_2.set_sign(3, "o")
        self.assertTrue(game_2.check_win_condition())

    def test_on_draw(self):
        game_3 = Game()
        game_3.set_sign(1, "x")
        game_3.set_sign(2, "o")
        game_3.set_sign(3, "o")
        self.assertFalse(game_3.check_win_condition())
        game_3.set_sign(4, "o")
        game_3.set_sign(5, "x")
        game_3.set_sign(6, "x")
        self.assertFalse(game_3.check_win_condition())
        game_3.set_sign(7, "o")
        game_3.set_sign(8, "x")
        game_3.set_sign(9, "o")
        self.assertFalse(game_3.check_win_condition())


if __name__ == "__main__":
    unittest.main()
