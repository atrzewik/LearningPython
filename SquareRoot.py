from FileOperator import FileOperator
numbers = FileOperator("data19.txt").change_to_integer()

index = 1
result = 1
for i in range(0, numbers[0]):
    if numbers[index+1] == 0:
        result = 1
    else:
        for x in range(0, numbers[index+1]):
            result = ((result + (numbers[index]/result))/2)
    index += 2
    print(result, end= " ")
    result = 1