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
        for column_number in range(self.number_of_fields):
            count = 0
            for row_number in range(self.number_of_fields):
                if self.fields[row_number][column_number] == sign:
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
        self.board = Board(UserInputProvider().collect_int_in_range_from_user(2, 20, "Please pick number of fields from 2 to 20: "))
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
        maximum_pick = self.board.number_of_fields - 1
        row = UserInputProvider().collect_int_in_range_from_user(0, maximum_pick, "Please, enter your row(0-%s) for %s:" % (maximum_pick, sign))
        column = UserInputProvider().collect_int_in_range_from_user(0, maximum_pick, "Please, enter your column(0-%s) for %s:" % (maximum_pick, sign))
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
            print("Draw!")
            return False
        else:
            return True

