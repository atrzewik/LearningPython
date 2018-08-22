from FileOperator import FileOperator
numbers = FileOperator("data/data7.txt").change_to_integer()
print("My data is: ", end= " ")
print(numbers)

def operation(numbers):
    index = 1
    result = []
    for i in range(0, numbers[0]):
        operations = ((numbers[index] * numbers[index+1]) + numbers[index+2])
        result.append(operations)
        index += 3
    return result


print("My numbers are: ", operation(numbers))

number = operation(numbers)
sum = ""
for num in number:
    value = 0
    while num > 0:
        value += num % 10
        num = int(num / 10)
    sum += " " + str(value)
print("My sum is: ", sum)
