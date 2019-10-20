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
		self.current_turn = "x"

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
				print("Crosses wins!!!")
                return True
            if all(element in self.noliki for element in combination):
				print("Noughts wins!!!")				
				return True
		return False

    def check_input(self, player_turn):
		try:
			player_turn = int(player_turn)
			return True
		except ValueError:
			print("Please enter a number [1-9]")
			return False

	def check_free_cell(self, player_turn):
		if player_turn not in self.crestiki and player_turn not in self.noliki:
			return True
		else:
			print("Please enter a free cell...")
			return False 

	def make_turn(self, cell):
		if self.check_input(cell) and self.check_free_cell(cell):
			self.set_sign(cell, self.current_turn)
			self.display()
			return True
		return False

	def run_game(self):
		print("To make a turn enter cell number")
		print("   |   |   ")
		print(" 1 | 2 | 3 ")
		print("___|___|___")
		print("   |   |   ")
		print(" 4 | 5 | 6 ")
		print("___|___|___")
		print("   |   |   ")
		print(" 7 | 8 | 9 ")
		print("   |   |   ")
		print("Player who enters crosses starts first")
		while True:
			if input("Enter \"start\" to start a game: ") == "start":
				break
		print("Game is starting\n\n")
		self.display()
		print("\n")
		while True:
			if self.make_turn(input("Crosses: " if self.current_turn == "x" else "Noughts: ")):
				if self.check_win_condition():
					break
				self.current_turn = "o"
