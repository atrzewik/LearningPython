from FileOperator import FileOperator
numbers = FileOperator("data/data1.txt").get_data_splitted_by_separator()
print(numbers)

index = 1
result = ""
for i in range(0, int(numbers[0])):
    if int(numbers[index]) < int(numbers[index + 1]):
        result += " " + str(numbers[index])
        index += 2
    else:
        result += " " + str(numbers[index + 1])
        index += 2
print(result)
