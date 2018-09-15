from UserInput import *


class Board(object):

    def __init__(self, number_of_fields):
        self.number_of_fields = number_of_fields
        self.capacity = self.calculate_capacity()
        self.fields = []
        for i in range(number_of_fields):
            self.fields.append(["-"] * number_of_fields)

    def __str__(self):
        new_board = ""
        for row in self.fields:
            new_board += " ".join(row) + "\n"
        return new_board

    def calculate_capacity(self):
        return self.number_of_fields * self.number_of_fields

    def mark_field(self, row, column, sign):
        if self.fields[row][column] != "-":
            raise AttributeError("This field %s, %s is busy." % (row, column))
        else:
            self.fields[row][column] = sign

    def row_winning_condition(self, sign):
        for row_number in range(self.number_of_fields):
            count = 0
            for column_number in range(self.number_of_fields):
                if self.fields[row_number][column_number] == sign:
                    count += 1
            if count == self.number_of_fields:
                return True

    def column_winning_condition(self, sign):
        for row_number in range(self.number_of_fields):
            count = 0
            for column_number in range(self.number_of_fields):
                if self.fields[column_number][row_number] == sign:
                        count += 1
            if count == self.number_of_fields:
                return True

    def diagonal_top_condition(self, sign):
        maximum_value_of_column = self.number_of_fields-1
        count = 0
        for column_number in range(self.number_of_fields):
            if self.fields[column_number][maximum_value_of_column-column_number] == sign:
                count += 1
        if count == self.number_of_fields:
            return True

    def diagonal_down_condition(self, sign):
        count = 0
        for column_number in range(self.number_of_fields):
            if self.fields[column_number][column_number] == sign:
                count += 1
        if count == self.number_of_fields:
            return True

    def check_the_winner(self, sign):
        return self.row_winning_condition(sign) or self.column_winning_condition(sign) or self.diagonal_top_condition(
            sign) or self.diagonal_down_condition(sign)


class Game(object):

    def __init__(self):
        self.turn = 0
        print("Hello!", "\n ...")
        self.board = Board(UserInput().get_number_of_fields())
        while True:
            print("Turn: ", self.turn)
            print(self.board)
            self.make_move()
            if not self.continue_game():
                print(self.board)
                break
            self.turn += 1

    def whose_move(self):
        if self.turn % 2 == 0:
            return "o"
        else:
            return "x"

    def make_move(self):
        sign = self.whose_move()
        row = UserInput().get_parameters(self.board.number_of_fields, "row", sign)
        column = UserInput().get_parameters(self.board.number_of_fields, "column", sign)
        try:
            self.board.mark_field(row, column, sign)
        except AttributeError:
            print(AttributeError)
            print("You pick wrong answer! Try again")
            self.make_move()

    def continue_game(self):
        sign = self.whose_move()
        if self.board.check_the_winner(sign):
            print("The winner is %s" % sign)
            return False
        elif self.turn == self.board.capacity:
            print("Remis!")
            return False
        else:
            return True


print(Game())

# def test_winning_condition_row():
#     number_of_fields = 10
#     board = Board(number_of_fields)
#     for column in range(number_of_fields):
#         board.mark_field(0, column, 'O')
#     print("ROW CONDITION")
#     print(board)
#     assert board.row_winning_condition('O')
#     print("test_winning_condition_row SUCCESS")
#
#
# def test_winning_condition_column():
#     number_of_fields = 10
#     board = Board(number_of_fields)
#     for row in range(number_of_fields):
#         board.mark_field(row, 0, 'O')
#     print("COLUMN CONDITION")
#     print(board)
#     assert board.column_winning_condition('O')
#     print("test_winning_condition_column SUCCESS")
#
#
# def test_winning_condition_diagonal_top():
#     number_of_fields = 10
#     board = Board(number_of_fields)
#     for row in range(number_of_fields):
#         board.mark_field(row, row, 'O')
#     print("DIAGONAL TOP CONDITION")
#     print(board)
#     assert board.diagonal_down_condition('O')
#     print("test_winning_condition_diagonal_top SUCCESS")
#
#
# def test_winning_condition_diagonal_down():
#     number_of_fields = 10
#     board = Board(number_of_fields)
#     for column in range(number_of_fields):
#         board.mark_field((number_of_fields - column - 1), column, 'O')
#     print("DIAGONAL DOWN CONDITION")
#     print(board)
#     assert board.diagonal_top_condition('O')
#     print("test_winning_condition_diagonal_down SUCCESS")
#
#
# print(test_winning_condition_row())
# print(test_winning_condition_column())
# print(test_winning_condition_diagonal_top())
# print(test_winning_condition_diagonal_down())