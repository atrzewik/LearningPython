from time import sleep


class Board(object):

    def __init__(self, number_of_fields):
        fields = []
        for i in range(number_of_fields):
            fields.append(["-"]*number_of_fields)
        self.fields = fields

    def __str__(self):
        new_board = ""
        for row in self.fields:
            new_board += " ".join(row) + "\n"
        return new_board

    def co_ordinates_of_signs(self, number_of_fields, sign, field):
        list_of_signs = []
        for i in range(number_of_fields):
            for j in range(number_of_fields):
                if field[i][j] == sign:
                    list_of_signs.append([i, j])
        return list_of_signs

    def return_true_or_false(self, number_of_fields, winning, sign, field):
        list_of_signs = self.co_ordinates_of_signs(number_of_fields, sign, field)
        for i in range(len(list_of_signs)):
            for j in range(2):
                count = 0
                for sign in list_of_signs:
                    if sign in winning:
                        count += 1
                if count == number_of_fields:
                    return True
                else:
                    return False

    def row_winning_condition(self, number_of_fields, sign, field):
        winning = []
        x, y = 0, 0
        for i in range(number_of_fields):
            winning.append([x, y + i])
        return self.return_true_or_false(number_of_fields, winning, sign, field)

    def column_winning_condition(self, number_of_fields, sign, field):
        winning = []
        x, y = 0, 0
        for i in range(number_of_fields):
            winning.append([x + i, y])
        return self.return_true_or_false(number_of_fields, winning, sign, field)

    def diagonal_top_condition(self, number_of_fields, sign, field):
        winning = []
        x, y = 0, 0
        for i in range(number_of_fields):
            winning.append([x + i, y + (number_of_fields - 1) - i])
        return self.return_true_or_false(number_of_fields, winning, sign, field)

    def diagonal_down_condition(self, number_of_fields, sign, field):
        winning = []
        x, y = 0, 0
        for i in range(number_of_fields):
            winning.append([x + i, y + i])
        return self.return_true_or_false(number_of_fields, winning, sign, field)

    def check_the_winner(self, number_of_fields, sign, field):
        if self.row_winning_condition(number_of_fields, sign, field) or self.column_winning_condition(number_of_fields, sign, field) or self.diagonal_top_condition(number_of_fields, sign, field) or self.diagonal_down_condition(number_of_fields, sign, field):
            return True
        else:
            return False


class Game(object):

    def __init__(self):
        answer = True
        print("Hello!", "\n ...")
        sleep(1)
        while answer:
            number_of_fields = int(input("Please pick number of fields from 2 to 20: "))
            self.fields = Board(number_of_fields).fields
            self.board = Board(number_of_fields)
            print(self.board)
            maximum_pick = number_of_fields - 1
            if number_of_fields < 2 or number_of_fields > 20:
                print("Wrong number!")
                answer = True
            else:
                for i in range(self.board_capacity(number_of_fields)):
                    moving = True
                    while moving:
                        sign = self.whose_move(i)
                        print("Turn: ", self.turn_number(i))
                        row = input("Please, enter your row(0-%s) for %s:" % (maximum_pick, sign))
                        column = input("Please, enter your column(0-%s) for %s:" % (maximum_pick, sign))
                        moving = self.make_move(row, column, maximum_pick)
                        if moving:
                            continue
                        else:
                            self.fields[int(row)][int(column)] = sign
                            field = self.fields
                            if self.continue_game(number_of_fields, sign, i, field):
                                print(self.board)
                            else:
                                if self.turn_number(i) == self.board_capacity(number_of_fields):
                                    print(self.board)
                                    print("Remis!")
                                elif Board(number_of_fields).check_the_winner(number_of_fields, sign, field):
                                    print(self.board)
                                    print("%s win!" % sign)
                                    break
                answer = False

    def board_capacity(self, number_of_fields):
        capacity = number_of_fields * number_of_fields
        return capacity

    def turn_number(self, turn):
        turns = 1
        turns += turn
        return turns

    def make_move(self, row, column, maximum_pick):
        answer = True
        if (int(row) or int(column)) > maximum_pick or (int(row) or int(column)) < 0:
            print("You pick wrong answer! Try again", "\n", self.board)
        elif self.fields[int(row)][int(column)] != "-":
            print("Occupaied!, Try again", "\n", self.board)
        else:
            answer = False
        return answer

    def continue_game(self, number_of_fields, sign, turns, field):
        if self.board.check_the_winner(number_of_fields, sign, field):
            return False
        elif self.turn_number(turns) == self.board_capacity(number_of_fields):
            return False
        else:
            return True

    def whose_move(self, turns):
        turn = self.turn_number(turns)
        if turn % 2 != 0:
            sign = "o"
        else:
            sign = "x"
        return sign


print(Game())
