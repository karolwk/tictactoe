import random
import copy


class StaticMethods:

    @staticmethod
    def check_field(cords, board) -> bool:
        # Check for "X" or "O" in specified field
        if board[cords[0]][cords[1]] in ("X", "O"):
            return True
        else:
            return False

    @staticmethod
    def change_sign(sign):
        if sign == "O":
            return "X"
        else:
            return "O"

    @staticmethod
    def check_draw(board: []) -> bool:
        if all([x.count("_") == 0 for x in board]):
            print("Draw")
            return True
        return False

    @staticmethod
    def check_win(board: []) -> bool:
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
                return True
        return False

    @staticmethod
    def print_board(board: []):
        # Print board accordly to instructions
        print(f"""{9 * "-"}
| {board[0][2]} {board[1][2]} {board[2][2]} |
| {board[0][1]} {board[1][1]} {board[2][1]} |
| {board[0][0]} {board[1][0]} {board[2][0]} |   
{9 * "-"}""")


class Player:
    def __init__(self):
        self.player = ""
        self.board = []
        self.sign = ""

    def _medium_ai_move(self, sign) -> []:
        # Creating temporary boards and checking for win in specified cords for two different signs.
        # First it returns cords for wining condition, secondly for blocking opponent wining move
        # If it fails it behave as Easy AI
        temp_board = copy.deepcopy(self.board)
        for _ in range(2):
            for i in range(3):
                for n in range(3):
                    if self.board[i][n] == "_":
                        temp_board[i][n] = sign
                        if StaticMethods.check_win(temp_board):
                            return [i, n]
                        else:
                            temp_board[i][n] = "_"
            sign = StaticMethods.change_sign(sign)
        return self._easy_ai_move()

    def _easy_ai_move(self) -> []:
        # Returns random cords
        while True:
            move = [random.randrange(0, 3), random.randrange(0, 3)]
            if not StaticMethods.check_field(move, self.board):
                return move

    def make_move(self, player, board, sign) -> None:
        self.board = board[:]
        self.player = player
        self.sign = sign

        if player == "easy":
            # Making move for "Easy" AI - AI makes only random decisions
            move = self._easy_ai_move()
            self.board[int(move[0])][int(move[1])] = sign
            print(f'Making move level {player}')
            StaticMethods.print_board(self.board)
        if player == "medium":
            # Making move for "Medium" AI
            move = self._medium_ai_move(sign)
            self.board[int(move[0])][int(move[1])] = sign
            print(f'Making move level {player}')
            StaticMethods.print_board(self.board)
        if player == "user":
            # Human player logic
            while True:
                cords = input("Enter the coordinates: >").split()
                if cords[0].isdigit() and cords[1].isdigit():
                    if (int(cords[0]) > 3) or (int(cords[1]) > 3):
                        print("Coordinates should be from 1 to 3!")
                    elif not StaticMethods.check_field([int(cords[0]) - 1, int(cords[1]) - 1], self.board):
                        self.board[int(cords[0]) - 1][int(cords[1]) - 1] = sign
                        StaticMethods.print_board(self.board)
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("You should enter numbers!")

    def return_board(self) -> []:
        return self.board


class TicTacToe:

    def __init__(self):
        self.board = []
        self.sign = "X"
        self._parameters = ('user', 'easy', 'medium', 'hard', 'exit', 'start')
        self._quit = False
        self._reset_board()

    def _check_parameters(self, *args) -> bool:
        # Checking parameters if they are in tuple "_parameters"
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

    def _reset_board(self) -> None:
        self.board = [["_" for x in range(3)] for i in range(3)]
        self.sign = StaticMethods.change_sign(self.sign)

    def play_game(self):
        # Main game method
        player1 = Player()
        player2 = Player()
        while True:
            user_input = input("Input command: ").split()
            if not self._check_parameters(*user_input):
                self.sign = "X"
                StaticMethods.print_board(self.board)
                while not self._quit:
                    if not StaticMethods.check_win(self.board):
                        if not StaticMethods.check_draw(self.board):
                            player1.make_move(user_input[1], self.board, self.sign)
                            self.sign = StaticMethods.change_sign(self.sign)
                            self.board = player1.return_board()[:]
                            if not StaticMethods.check_win(self.board):
                                if not StaticMethods.check_draw(self.board):
                                    player2.make_move(user_input[2], self.board, self.sign)
                                    self.sign = StaticMethods.change_sign(self.sign)
                                    self.board = player1.return_board()[:]
                                else:
                                    self._reset_board()
                                    break
                            else:

                                self._reset_board()
                                print(f"{self.sign} wins")
                                break
                        else:
                            self._reset_board()
                            break
                    else:

                        self._reset_board()
                        print(f"{self.sign} wins")
                        break
            if self._quit:
                break


game = TicTacToe()
game.play_game()
