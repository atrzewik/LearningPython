from FileOperator import FileOperator
numbers = FileOperator("data/data24.txt").change_to_integer()


class SavingsCalculator(object):

    def __init__(self, data):
        self.one = data[0]
        self.data = data[1:]

    def calculator(self):
        index = 0
        result = ""
        for i in range (0, self.one):
            year = 0
            sum = self.data[index]
            while self.data[index+1] > sum :
                product = sum * (self.data[index+2] / 100)
                sum += product
                year += 1
            result += " " + str(year)
            index += 3
        return result


print(SavingsCalculator(numbers).calculator())