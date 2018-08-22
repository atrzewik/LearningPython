from FileOperator import FileOperator
numbers = FileOperator("data/data4.txt").change_to_integer()
index = 1
for x in range(0,numbers[0]):
    divide = numbers[index]/numbers[index + 1]
    divide = round(divide)
    print(divide, end=" ")
    index += 2