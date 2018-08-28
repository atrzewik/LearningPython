from FileOperator import FileOperator
signs = FileOperator("data/data27.txt").get_data_splitted_by_separator()


class LifeIsSimple(object):

    def __init__(self, data):
        self.data = data

    def making_data_as_lists(self):
        lists = []
        for elements in self.data:
            one_list = []
            for element in elements:
                one_list.append(element)
            lists.append(one_list)
        return lists

    def board(self):
        places = []
        for i in range(11):
            places.append(["-"] * 13)
        return places

    def next_generation_board(self, data):
        board = self.board()
        index_y = 3
        for y in range(0, 5):
            index_x = 3
            for x in range(0, 7):
                board[index_y][index_x] = data[y][x]
                index_x += 1
            index_y += 1
        return board

    def neighbours(self):
        assuming = ""
        next_generation = self.board()
        board = self.next_generation_board(self.making_data_as_lists())
        alive = "X"
        dead = "-"
        for i in range(5):
            sums = 0
            for x in range(10):
                for y in range(12):
                    population = 0
                    if board[x - 1][y - 1] == alive:
                        population += 1
                    if board[x][y - 1] == alive:
                        population += 1
                    if board[x + 1][y - 1] == alive:
                        population += 1
                    if board[x - 1][y] == alive:
                        population += 1
                    if board[x + 1][y] == alive:
                        population += 1
                    if board[x - 1][y + 1] == alive:
                        population += 1
                    if board[x][y + 1] == alive:
                        population += 1
                    if board[x + 1][y + 1] == alive:
                        population += 1
                    if board[x][y] == alive and (population < 2 or population > 3):
                        next_generation[x][y] = dead
                    elif board[x][y] == alive and (population == 3 or population == 2):
                        next_generation[x][y] = alive
                        sums += 1
                    elif board[x][y] == dead and population == 3:
                        next_generation[x][y] = alive
                        sums += 1
            assuming += " " + str(sums)
            board = next_generation
            next_generation = self.board()
        return assuming


print(LifeIsSimple(signs).neighbours())
