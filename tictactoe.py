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
    def avail_spots(board) -> []:
        return [x for x in board if isinstance(x, int)]

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
    def check_win(board: [], sign) -> bool:
        # Checking win or draw condition for hard coded situations
        # Return 'True' in case of win

        is_matrix = all(isinstance(ele, list) for ele in board)
        if not is_matrix:
            # Making matrix
            board = [[board[i + x] for x in range(3)] for i in range(0, 8, 3)]

        if (board[0][0] == sign) and (board[1][1] == sign) and (board[2][2] == sign):
            return True
        if (board[0][2] == sign) and (board[1][1] == sign) and (board[2][0] == sign):
            return True
        for i in range(3):
            if (board[i][0] == sign) and (board[i][1] == sign) and (board[i][2] == sign):
                return True
            if (board[0][i] == sign) and (board[1][i] == sign) and (board[2][i] == sign):
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
        self.first_player = ""
        self.second_player = ""

    def _easy_ai_move(self) -> []:
        # Returns random cords
        while True:
            move = [random.randrange(0, 3), random.randrange(0, 3)]
            if not StaticMethods.check_field(move, self.board):
                return move

    def _medium_ai_move(self, sign) -> []:
        # Creating temporary board and checking for win in specified cords for two different signs.
        # First it returns cords for wining condition, secondly for blocking opponent wining move
        # If it fails it behave as Easy AI
        temp_board = copy.deepcopy(self.board)
        for _ in range(2):
            for i in range(3):
                for n in range(3):
                    if self.board[i][n] == "_":
                        temp_board[i][n] = sign
                        if StaticMethods.check_win(temp_board, sign):
                            return [i, n]
                        else:
                            temp_board[i][n] = "_"
            sign = StaticMethods.change_sign(sign)
        return self._easy_ai_move()

    def _hard_ai_move(self, sign) -> []:
        # Finds the best move based on MiniMax Algorithm in Game Theory
        self.first_player = sign
        self.second_player = StaticMethods.change_sign(sign)
        # Cords that we return up accordingly with number/key we get from min_max
        cords = {0: [0, 2], 1: [1, 2], 2: [2, 2], 3: [0, 1], 4: [1, 1], 5: [2, 1], 6: [0, 0], 7: [1, 0], 8: [2, 0]}
        # Creating new board for AI
        new_board = [["_" for x in range(3)] for i in range(3)]
        # Filling new board with data from original board in correct order for algorithm
        for x in range(3):
            for y in range(3):
                new_board[2 - y][x] = self.board[x][y]
        # Creating one dimension board
        new_board = [new_board[n][i] for n in range(3) for i in range(3)]
        # Changing "_" to index numbers
        new_board = [num if value == "_" else value for num, value in enumerate(new_board)]
        results = self._min_max(new_board, sign)[0]
        return cords[results]

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
        if player == "hard":
            move = self._hard_ai_move(sign)
            self.board[move[0]][move[1]] = sign
            print(f'Making move level {player}')
            StaticMethods.print_board(self.board)
        if player == "user":
            # Human player logic
            while True:
                cords = input("Enter the coordinates: >").split()
                if len(cords) == 2 and cords[0].isdigit() and cords[1].isdigit():
                    if (int(cords[0]) > 3) or (int(cords[1]) > 3):
                        print("Coordinates should be from 1 to 3!")
                    elif not StaticMethods.check_field([int(cords[0]) - 1, int(cords[1]) - 1], self.board):
                        self.board[int(cords[0]) - 1][int(cords[1]) - 1] = sign
                        StaticMethods.print_board(self.board)
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("You should enter numbers from 1 to 3 separated with space for example: '1 2'!")

    def _min_max(self, board: [], player: str) -> ():
        # Making list of available spots (index numbers)
        spots = StaticMethods.avail_spots(board)
        if StaticMethods.check_win(board, self.first_player):
            return 0, 10
        if StaticMethods.check_win(board, self.second_player):
            return 0, -10
        if len(spots) == 0:
            return 0, 0
        # dictionary that contains each move and values {board_index: value}
        moves = {}
        for value in spots:
            # loop through available spots and fill 'moves' dict with indexes and values
            moves[value] = value
            board[value] = player
            if player == self.first_player:
                result = self._min_max(board, self.second_player)
                moves[value] = result[-1]
            else:
                result = self._min_max(board, self.first_player)
                moves[value] = result[-1]
            # reset board to original value
            board[value] = value
        # tuple to return with best position and value
        best_value = ()
        # searching for best value depending on player that is playing
        if player == self.first_player:
            temp = -1000
            for index, value in moves.items():
                if value > temp:
                    temp = value
                    best_value = (index, value)
        if player == self.second_player:
            temp = 1000
            for index, value in moves.items():
                if value < temp:
                    temp = value
                    best_value = (index, value)
        return best_value

    def return_board(self) -> []:
        return self.board


class TicTacToe:

    def __init__(self):
        self.board = []
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

    def play_game(self):
        # Main game method
        player1 = Player()
        player2 = Player()
        while True:
            user_input = input("Input command: ").split()
            if not self._check_parameters(*user_input):
                StaticMethods.print_board(self.board)
                while not self._quit:
                    if not StaticMethods.check_win(self.board, "O"):
                        if not StaticMethods.check_draw(self.board):
                            player1.make_move(user_input[1], self.board, "X")
                            self.board = player1.return_board()
                            if not StaticMethods.check_win(self.board, "X"):
                                if not StaticMethods.check_draw(self.board):
                                    player2.make_move(user_input[2], self.board, "O")
                                    self.board = player1.return_board()
                                else:
                                    self._reset_board()
                                    break
                            else:
                                print("X wins")
                                self._reset_board()
                                break
                        else:
                            self._reset_board()
                            break
                    else:
                        print("O wins")
                        self._reset_board()
                        break
            if self._quit:
                break


game = TicTacToe()
game.play_game()
