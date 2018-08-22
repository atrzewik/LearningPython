from FileOperator import FileOperator
numbers = FileOperator("data14.txt").change_to_integer()
print(numbers)


class Average(object):
    def __init__(self, value):
        self.value = value[1:]

    def averged(self):
        value = self.value
        lists = ""
        listed =[]
        sums = 0
        for number in value:
            if number != 0:
                listed.append(number)
            else:
                sums += sum(listed)/len(listed)
                sums = round(sums)
                lists += " " + str(sums)
                sums = 0
                listed = []
        return lists


print("Averge :", Average(numbers).averged())