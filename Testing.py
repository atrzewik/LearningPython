from CircleAndCross import *


def test_winning_condition_row():
    number_of_fields = 10
    board = Board(number_of_fields)
    for row in range(number_of_fields):
        for column in range(number_of_fields):
            board.mark_field(row, column, 'O')
        print("ROW CONDITION")
        print(board)
        assert board.row_winning_condition('O')
        board = Board(number_of_fields)
        print("test_winning_condition_row SUCCESS")


def test_winning_condition_column():
    number_of_fields = 10
    board = Board(number_of_fields)
    for column in range(number_of_fields):
        for row in range(number_of_fields):
            board.mark_field(row, column, 'O')
        print("COLUMN CONDITION")
        print(board)
        assert board.column_winning_condition('O')
        board = Board(number_of_fields)
        print("test_winning_condition_column SUCCESS")


def test_winning_condition_diagonal_top():
    number_of_fields = 10
    board = Board(number_of_fields)
    for row in range(number_of_fields):
        board.mark_field(row, row, 'O')
    print("DIAGONAL TOP CONDITION")
    print(board)
    assert board.diagonal_down_condition('O')
    print("test_winning_condition_diagonal_top SUCCESS")


def test_winning_condition_diagonal_down():
    number_of_fields = 10
    board = Board(number_of_fields)
    for column in range(number_of_fields):
        board.mark_field((number_of_fields - column - 1), column, 'O')
    print("DIAGONAL DOWN CONDITION")
    print(board)
    assert board.diagonal_top_condition('O')
    print("test_winning_condition_diagonal_down SUCCESS")


print(test_winning_condition_row())
print(test_winning_condition_column())
print(test_winning_condition_diagonal_top())
print(test_winning_condition_diagonal_down())
