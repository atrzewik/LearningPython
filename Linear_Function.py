from FileOperator import FileOperator
numbers = FileOperator("data16.txt").change_to_integer()


class LinearFunction(object):
    def __init__(self, value):
        self.values = value[1:]

    def equation(self):
        values = self.values
        index = 0
        ab_values = ""
        while index < len(values):
            x1 = values[index]
            y1 = values[index+1]
            x2 = values[index+2]
            y2 = values[index+3]
            a = (y2 - y1)/(x2 - x1)
            b = y1 - (a*x1)
            a = round(a)
            b = round(b)
            ab_values += "(" + str(a) + " " + str(b) + ") "
            index += 4
        return ab_values

print(LinearFunction(numbers).equation())