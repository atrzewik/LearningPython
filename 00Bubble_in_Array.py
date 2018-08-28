from FileOperator import FileOperator
numbers = FileOperator("data/data23.txt").change_to_integer()


class BubbleInArray(object):

    def __init__(self, data):
        self.data = data

    def bubble(self):
        new_data = []
        swap = 0
        index = 0
        for i in range(0, len(self.data)-1):
            n1 = self.data[index]
            n2 = self.data[index+1]
            if n2 == -1:
                new_data.append(n1)
            elif n1 <= n2:
                new_data.append(n1)
            else:
                self.data[index] = n2
                self.data[index+1] = n1
                swap += 1
                new_data.append(n2)
            index += 1
        return swap, new_data

    def checksum(self):
        two_data = self.bubble()
        data, swap = two_data[1], two_data[0]
        result = 0
        for i in range(0, len(data)):
            result += data[i]
            result *= 113
            result %= 10000007
        return str(swap) + " " + str(result)


print(BubbleInArray(numbers).checksum())

