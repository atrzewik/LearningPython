from FileOperator import FileOperator
numbers = FileOperator("data/data8.txt").change_to_integer()


def sorted_numbers(numbers):
    index = 1
    string_of_mediana = ""
    for i in range(0, numbers[0]):
        three_numbers = []
        three_numbers += numbers[index:index + 3]
        three_numbers = sorted(three_numbers)
        median = three_numbers[1]
        string_of_mediana += " " + str(median)
        index += 3
    return string_of_mediana


print("Median: ", end=" ")
print(sorted_numbers(numbers))