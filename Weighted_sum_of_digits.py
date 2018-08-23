from FileOperator import FileOperator
numbers = FileOperator("data/data12.txt").change_to_integer()

def weighted_sum(data):
    weighted = ""
    for number in data[1:]:
        sum = 0
        number = str(number)
        for i in range(0, len(number)):
            sum += (int(number[i]) * (i+1))
        weighted += " " + str(sum)
    return weighted


print(weighted_sum(numbers))