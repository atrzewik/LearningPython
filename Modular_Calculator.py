from FileOperator import FileOperator
numbers = FileOperator("data/data18.txt").get_data_splitted_by_separator("\n")


class ModularCalculator(object):

    def __init__(self, data):
        self.modulo = data[len(data)-1]
        self.result = data[0]
        self.data = data[1:len(data)-1]

    def calculate(self):
        result = int(self.result)
        data = self.data
        for digit in data:
            if digit[0] == "+" :
                result += int(digit[2:])
            else:
                result *= int(digit[2:])
        return result

    def modular(self):
        modulo = self.modulo
        value = self.calculate() % int(modulo[2:])
        return value


print(ModularCalculator(numbers).modular())
