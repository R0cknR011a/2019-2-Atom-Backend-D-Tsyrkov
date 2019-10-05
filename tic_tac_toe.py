from crestiki_noliki import Game

game = Game()
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
remaining_cells = [number for number in range(1, 10)]
game.display()
print("\n")
while True:
    while True:
        while True:
            player_turn = input("Crosses: ")
            try:
                player_turn = int(player_turn)
                break
            except ValueError:
                print("Please enter a number [1-9]")
        if player_turn in remaining_cells:
            remaining_cells.remove(player_turn)
            game.set_sign(player_turn, "x")
            break
        else:
            print("Please choose a free cell")
    game.display()
    print("\n")
    if game.check_win_condition() == "crestiki":
        print("Player_1 wins")
        break
    elif not remaining_cells:
        print("Draw")
        break
    while True:
        while True:
            player_turn = input("Noughts: ")
            try:
                player_turn = int(player_turn)
                break
            except ValueError:
                print("Please enter a number [1-9]")
        if player_turn in remaining_cells:
            remaining_cells.remove(player_turn)
            game.set_sign(player_turn, "o")
            break
        else:
            print("Please choose a free cell")
    game.display()
    print("\n")
    if game.check_win_condition() == "noliki":
        print("Player_2 wins")
        break
    elif not remaining_cells:
        print("Draw")
        break
    

