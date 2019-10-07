class Game:

    def __init__(self):
        self.field = [
            "   |   |   ",
            "   |   |   ",
            "___|___|___",
            "   |   |   ",
            "   |   |   ",
            "___|___|___",
            "   |   |   ",
            "   |   |   ",
            "   |   |   "
        ]

        self.map = {
            7: (7, 1),
            8: (7, 5),
            9: (7, 9),
            4: (4, 1),
            5: (4, 5),
            6: (4, 9),
            1: (1, 1),
            2: (1, 5),
            3: (1, 9)
        }

        self.win_combinations = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]

        self.crestiki = []
        self.noliki = []

    def display(self):
        for row in self.field:
            print(row)

    def set_sign(self, cell, sign):
        if sign == "x":
            self.crestiki.append(cell)
        elif sign == "o":
            self.noliki.append(cell)
        row = self.map[cell][0]
        column = self.map[cell][1]
        self.field[row] = self.field[row][:column] +\
            sign.capitalize() + self.field[row][column + 1:]

    def check_win_condition(self):
        for combination in self.win_combinations:
            if all(element in self.crestiki for element in combination):
                return "crestiki"
            if all(element in self.noliki for element in combination):
                return "noliki"
        return False
