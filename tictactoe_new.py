import random


class TicTacToe:

    def __init__(self):
        self.board = [["_" for x in range(3)] for i in range(3)]
        self.player = "X"

    def _check_field(self, cords) -> bool:
        if self.board[int(cords[0]) - 1][int(cords[1]) - 1] in ("X", "O"):
            return True
        else:
            return False

    def _ai_play(self, difficulty: str) -> None:
        if difficulty == "easy":
            self.player = "O"
            while True:
                move = [random.randrange(0, 3), random.randrange(0, 3)]
                if not self._check_field(move):
                    self.board[int(move[0]) - 1][int(move[1]) - 1] = self.player
                    self.player = "X"
                    print('Making move level "easy"')
                    self._print_board()
                    break

    def _check_win(self) -> bool:
        # Checking win or draw condition for hard coded situations
        # Return 'False' if there are empty lines to fill and 'True' in case of win/draw
        win_group = ["".join(self.board[0][:3]), "".join(self.board[1][:3]), "".join(self.board[2][:3]),
                     self.board[0][0] + self.board[1][0] + self.board[2][0],
                     self.board[0][1] + self.board[1][1] + self.board[2][1],
                     self.board[0][2] + self.board[1][2] + self.board[2][2],
                     self.board[0][0] + self.board[1][1] + self.board[2][2],
                     self.board[0][2] + self.board[1][1] + self.board[2][0],
                     ]
        for x in win_group:
            if x.count("X") == 3 or x.count("O") == 3:
                print(f"{x[0]} wins")
                return True
        if all([x.count("_") == 0 for x in win_group]):
            print("Draw")
            return True
        return False

    def _print_board(self):
        # Print board accordly to instructions
        print(f"""{9 * "-"}
| {self.board[0][2]} {self.board[1][2]} {self.board[2][2]} |
| {self.board[0][1]} {self.board[1][1]} {self.board[2][1]} |
| {self.board[0][0]} {self.board[1][0]} {self.board[2][0]} |   
{9 * "-"}""")

    def play(self):
        self._print_board()
        while True:
            if not self._check_win():
                cords = input("Enter the coordinates: >").split()
                if cords[0].isdigit() and cords[1].isdigit():
                    if (int(cords[0]) > 3) or (int(cords[1]) > 3):
                        print("Coordinates should be from 1 to 3!")
                    elif not self._check_field(cords):
                        self.board[int(cords[0]) - 1][int(cords[1]) - 1] = self.player
                        self._print_board()
                        if not self._check_win():
                            self._ai_play("easy")
                        else:

                            break

                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("You should enter numbers!")
            else:
                break


game = TicTacToe()
game.play()

