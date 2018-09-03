class Board(object):

    def __init__(self):
        self.board = self.row_and_column()
        self.printed_board = self.print_board(self.board)
        self.circle = Field().circle
        self.cross = Field().cross

    def row_and_column(self):
        board = []
        for i in range(3):
            board.append(["-"]*3)
        return board

    def print_board(self, board):
        new_board = ""
        for row in board:
            new_board += " ".join(row) + "\n"
        return new_board

    def add_to_board(self, row, column, sign, board):
        board[int(row)][int(column)] = sign
        return self.print_board(board)

    def co_ordinates_of_signs(self, sign, board):
        list_of_signs = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == sign:
                    list_of_signs.append([i, j])
        return list_of_signs

    def check_the_winner(self, sign, board):
        list_of_signs = self.co_ordinates_of_signs(sign, board)
        wins = 0
        for i in range(len(list_of_signs)):
            for j in range(2):
                x = i
                y = j
                winning = [[[x, y], [x, y + 1], [x, y + 2]], [[x, y], [x + 1, y + 1], [x + 2, y + 2]], [[x, y + 2], [x + 1, y + 1], [x + 2, y]], [[x, y], [x + 1, y], [x + 2, y]]]
                for win in winning:
                    count = 0
                    for sign in list_of_signs:
                        if sign in win:
                            count += 1
                    if count == 3:
                        wins = 1
                        break
            return wins


class Field(object):

    def __init__(self):
        self.circle = self.circle_sign()
        self.cross = self.cross_sign()

    def circle_sign(self):
        circle = "o" or "O"
        return circle

    def cross_sign(self):
        cross = "x" or "X"
        return cross


class Game(object):

    def __init__(self):
        self.board = Board().row_and_column()
        self.print_board = Board().printed_board
        self.circle = Field().circle_sign()
        self.cross = Field().cross_sign()

    def moves(self):
        print(self.print_board)
        print("Hello!")
        winner = ""
        for i in range(9):
            if i % 2 == 0:
                row = input("Please, enter your row(0-2) for circle:")
                column = input("Please, enter your column(0-2) for circle:")
                if (int(row) or int(column)) > 2 or (int(row) or int(column)) < 0:
                    raise Exception("You pick wrong answer!")
                elif self.board[int(row)][int(column)] != "-":
                    raise Exception("This place is busy")
                else:
                    board = Board().add_to_board(row, column, self.circle, self.board)
                    check_win = Board().check_the_winner(self.circle, self.board)
                    print(board)
                    if check_win == 1:
                        winner += "Circle win!"
                        break
                    else:
                        continue
            else:
                row = input("Please, enter your row(0-2) for cross:")
                column = input("Please, enter your column(0-2) for cross:")
                if (int(row) or int(column)) > 2 or (int(row) or int(column)) < 0:
                    raise Exception("You pick wrong answer!")
                elif self.board[int(row)][int(column)] != "-":
                    raise Exception("This place is busy")
                else:
                    board = Board().add_to_board(row, column, self.cross, self.board)
                    check_win = Board().check_the_winner(self.cross, self.board)
                    print(board)
                    if check_win == 1:
                        winner += "Cross win!"
                        break
                    else:
                        continue
        return winner


print(Game().moves())
