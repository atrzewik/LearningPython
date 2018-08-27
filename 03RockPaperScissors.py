from FileOperator import FileOperator
sign = FileOperator("data/data26.txt").get_data_splitted_by_separator("\n")


class RockPaperScissors(object):

    def __init__(self, data):
        self.one = int(data[0])
        self.data = data[1:]
        lists = []
        index = 0
        for i in range(0, self.one):
            splitted = self.data[index].split()
            lists.append(splitted)
            index += 1
        self.lists = lists

    def first_player(self):
        all_scores = []
        index = 0
        for i in range(0, self.one):
            score = 0
            for match in self.lists[index]:
                if match == "RS" or match == "SP" or match == "PR":
                    score += 1
                else:
                    score += 0
            index += 1
            all_scores.append(score)
        return all_scores

    def second_player(self):
        all_scores = []
        index = 0
        for i in range(0, self.one):
            score = 0
            for match in self.lists[index]:
                if match == "SR" or match == "PS" or match == "RP":
                    score += 1
                else:
                    score += 0
            index += 1
            all_scores.append(score)
        return all_scores

    def who_wins(self):
        who_win =  ""
        first_player_score = self.first_player()
        second_player_score = self.second_player()
        for i in range(0, self.one):
            if first_player_score[i] > second_player_score[i]:
                who_win += " 1"
            elif first_player_score[i] < second_player_score[i]:
                who_win += " 2"
            else:
                continue
        return who_win


print(RockPaperScissors(sign).who_wins())

