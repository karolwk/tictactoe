board = []


def make_board():
    # Making starting board with empty lines "_"
    global board
    board = [["_" for x in range(3)] for i in range(3)]


def check_win() -> bool:
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


def print_board():
    # Print board accordly to instructions
    print(f"""{9 * "-"}
| {board[0][2]} {board[1][2]} {board[2][2]} |
| {board[0][1]} {board[1][1]} {board[2][1]} |
| {board[0][0]} {board[1][0]} {board[2][0]} |   
{9 * "-"}""")


def play():
    player = "X"
    print_board()
    while True:
        if not check_win():
            cords = input("Enter the coordinates: >").split()
            if cords[0].isdigit() and cords[1].isdigit():
                if (int(cords[0]) > 3) or (int(cords[1]) > 3):
                    print("Coordinates should be from 1 to 3!")
                elif not (board[int(cords[0]) - 1][int(cords[1]) - 1] in ("X", "O")):
                    if player == "X":
                        board[int(cords[0]) - 1][int(cords[1]) - 1] = player
                        player = "O"
                        print_board()
                    else:
                        board[int(cords[0]) - 1][int(cords[1]) - 1] = player
                        player = "X"
                        print_board()
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("You should enter numbers!")
                cords = input("Enter the coordinates: >").split()
        else:
            break


make_board()
play()
