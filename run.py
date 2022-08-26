from random import randint

score = {"Player": 0, "Computer": 0}


class Board:
    """
    Create instance of the board class
    """
    def __init__(self, name, size, num_ships, type):
        self.name = name
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.type = type
        self.ships = []
        self.shots = []

    def create_board(self):
        for row in self.board:
            print(" ".join(row))

    def add_ship(self, x, y):
        self.ships.append((x, y))
        self.board[x][y] = "!"
        # if self.type == "Player":
        #     self.board[x][y] = "!"

    def take_shot(self, x, y):
        self.shots.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            if self.type == "Player":
                score["Computer"] += 1
            else:
                score["Player"] += 1
            return "Hit"
        else:
            return "Miss"

    def return_shots(self, x, y):
        if (x, y) in self.shots:
            print("already fired there")
            return True
        else:
            print("not fired here")
            return False

    def return_ships(self, x, y):
        if (x, y) in self.ships:
            return True
        else:
            return False


def validate_input(input, max, type):
    """
    Checkes the input and validates it as int and sting or out of scope
    the valid_input is the min and max size allowed
    """
    valid_input = [4, 5, 6, 7, 8]
    try:
        num = int(input)

        if type == "start":
            if num not in valid_input:
                raise ValueError(
                    f"Must be {valid_input}, you put {num}"
                )
        elif type == "shot":
            if num not in range(0, max):
                raise ValueError(
                    f"Board size is {max}, you put {num}"
                )
    except ValueError as e:
        print(f"input is invalid {e}, please try again")
        return False

    return True


def add_ships_to_board(board):
    """
    Add player and computer ships to there boards using random.
    Also checks there is not a ship already there
    """
    while len(board.ships) < board.num_ships:
        num1 = return_num(board.size)
        num2 = return_num(board.size)
        if not board.return_ships(num1, num2):
            board.add_ship(num1, num2)


def return_num(num):
    """
    Returns a random number within the num and 0
    """

    return randint(0, num - 1)


def play_game(player, computer, size, num_ships):
    """
    prints the player/computer boards and waits for the player input to fire a shot.
    then the computer will randomly pick and fire a shot.
    once both shots have been fired the board will be displayed again with the hits or miss.
    """
    print(f"Board set to size: {size}X{size}")
    print(f"Min being 0 and max: {size - 1}")
    print(f"With {num_ships} ships Each")
    print("Grid x is row along, Grid Y is column down")
    print(f"{player.name} Board")
    player.create_board()
    print("_" * 30)
    print("Computer Board")
    computer.create_board()

    while True:

        while True:
            x = input("Please select grid X:\n")
            if validate_input(x, size, "shot"):
                break

        while True:
            y = input("Please select grid Y:\n")
            if validate_input(y, size, "shot"):
                break

        while True:
            if not computer.return_shots(x, y):
                computer.take_shot(int(x), int(y))
                break

        while True:
            x = return_num(size)
            y = return_num(size)

            if not player.return_shots(x, y):
                player.take_shot(int(x), int(y))
                break

        print(f"Board set to size: {size}X{size}")
        print(f"Min being 0 and max: {size - 1}")
        print(f"With {num_ships} ships Each")
        print("Grid x is row along, Grid Y is column down\n")
        print(score)
        print(f"{player.name} Board")
        player.create_board()
        print("_" * 30)
        print("Computer Board")
        computer.create_board()


def start_game():
    """
    Initialize the start function, ask for player name, board size.
    """

    print('Welcome to battleships, please have fun and remember to shout:')
    print('"YOU SUNK MY BATTLESHIP"\n')

    name = "Player"
    size = 4
    ships = 4

    # name = input("Please enter your name:\n")

    # while True:

    #     size = int(input("Please pick board size, Min 4: Max 8:\n"))
    #     if validate_input(size, 0, "start"):
    #         break

    # while True:

    #     ships = int(input("Please select number of ships, Min 4: Max 8:\n"))
    #     if validate_input(ships, 0, "start"):
    #         break

    player_b = Board(name, size, ships, "player")
    computer_b = Board("Computer", size, ships, "computer")

    for ship in range(ships):
        add_ships_to_board(player_b)
        add_ships_to_board(computer_b)

    play_game(player_b, computer_b, size, ships)


start_game()
