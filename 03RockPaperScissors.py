from FileOperator import FileOperator
sign = FileOperator("data/data26.txt").get_data_splitted_by_separator("\n")


class RockPaperScissors(object):

    def __init__(self, data):
        self.number_of_arguments = int(data[0])
        self.data = data[1:]
        self.lists = []
        index = 0
        for i in range(0, self.number_of_arguments):
            splitted = self.data[index].split()
            self.lists.append(splitted)
            index += 1

    def counting_scores(self, player):
        all_scores = []
        index = 0
        for i in range(0, self.number_of_arguments):
            score = 0
            for match in self.lists[index]:
                if player == 1:
                    if match == "RS" or match == "SP" or match == "PR":
                        score += 1
                elif player == 2:
                    if match == "SR" or match == "PS" or match == "RP":
                        score += 1
                else:
                    raise Exception("ERROR! You can use this function only if player is equal to 1 or 2.")
            index += 1
            all_scores.append(score)
        return all_scores

    def first_player(self):
        return self.counting_scores(1)

    def second_player(self):
        return self.counting_scores(2)

    def who_wins(self):
        who_win = ""
        first_player_score = self.first_player()
        second_player_score = self.second_player()
        for i in range(0, self.number_of_arguments):
            if first_player_score[i] > second_player_score[i]:
                who_win += " 1"
            elif first_player_score[i] < second_player_score[i]:
                who_win += " 2"
            else:
                continue
        return who_win


print(RockPaperScissors(sign).who_wins())
