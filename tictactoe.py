import random


class TicTacToe:

    def __init__(self):
        self.board = []
        self.sign = "X"
        self._parameters = ('user', 'easy', 'medium', 'hard', 'exit', 'start')
        self._quit = False
        self._reset_board()

    def _check_field(self, cords) -> bool:
        # Check for "X" or "O" in specified field
        if self.board[int(cords[0]) - 1][int(cords[1]) - 1] in ("X", "O"):
            return True
        else:
            return False

    def _check_parameters(self, *args) -> bool:
        # Checking parameters if they are in tuple
        for n in args:
            if n not in self._parameters:
                print('Bed parameters')
                return True
            if n == "exit":
                self._quit = True
                return True
        if 3 != len(args) != 1:
            print('Bed parameters')
            return True
        return False

    def _change_sign(self):
        if self.sign == "O":
            self.sign = "X"
        else:
            self.sign = "O"

    def _reset_board(self) -> None:
        self.board = [["_" for x in range(3)] for i in range(3)]

    def _players(self, player: str) -> None:
        # AI EASY
        if player == "easy":
            while True:
                move = [random.randrange(0, 3), random.randrange(0, 3)]
                if not self._check_field(move):
                    self.board[int(move[0]) - 1][int(move[1]) - 1] = self.sign
                    self._change_sign()
                    print('Making move level "easy"')
                    self._print_board()
                    break
        # Human player
        if player == "user":
            while True:
                cords = input("Enter the coordinates: >").split()
                if cords[0].isdigit() and cords[1].isdigit():
                    if (int(cords[0]) > 3) or (int(cords[1]) > 3):
                        print("Coordinates should be from 1 to 3!")
                    elif not self._check_field(cords):
                        self.board[int(cords[0]) - 1][int(cords[1]) - 1] = self.sign
                        self._change_sign()
                        self._print_board()
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("You should enter numbers!")

    @staticmethod
    def _check_win(board: []) -> bool:
        # Checking win or draw condition for hard coded situations
        # Return 'False' if there are empty lines to fill and 'True' in case of win/draw
        win_group = ["".join(board[0][:3]), "".join(board[1][:3]), "".join(board[2][:3]),
                     board[0][0] + board[1][0] + board[2][0],
                     board[0][1] + board[1][1] + board[2][1],
                     board[0][2] + board[1][2] + board[2][2],
                     board[0][0] + board[1][1] + board[2][2],
                     board[0][2] + board[1][1] + board[2][0],
                     ]
        for x in win_group:
            if x.count("X") == 3 or x.count("O") == 3:

                print(f"{x[0]} wins")
                return True
        if all([x.count("_") == 0 for x in win_group]):
            print("Draw")
            return True
        return False

    def play_game(self):
        while True:
            user_input = input("Input command: ").split()
            if not self._check_parameters(*user_input):
                self._print_board()
                while not self._quit:
                    if not self._check_win(self.board):
                        self._players(user_input[1])
                        if not self._check_win(self.board):
                            self._players(user_input[2])
                        else:
                            self._reset_board()
                            break
                    else:
                        self._reset_board()
                        break
            if self._quit:
                break

    def _print_board(self):
        # Print board accordly to instructions
        print(f"""{9 * "-"}
| {self.board[0][2]} {self.board[1][2]} {self.board[2][2]} |
| {self.board[0][1]} {self.board[1][1]} {self.board[2][1]} |
| {self.board[0][0]} {self.board[1][0]} {self.board[2][0]} |   
{9 * "-"}""")


game = TicTacToe()
game.play_game()
