from FileOperator import FileOperator
numbers = FileOperator("data15.txt").change_to_integer()
print(numbers)

class Array(object):
    def __init__(self, value):
        self.value = value
        self.value_out = value[1:]

    def checksum(self):
        data = self.value_out
        result = 0
        for i in range(0, self.value[0]):
            result += data[i]
            result *= 113
            result %= 10000007
        return result

print(Array(numbers).checksum())