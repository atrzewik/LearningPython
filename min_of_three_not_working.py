from FileOperator import FileOperator
numbers = FileOperator("data2.txt").change_to_integer()

print(numbers)

strings = ""
index = 1
for i in range(0, numbers[0]):
    first = numbers[index]
    second = numbers[index+1]
    third = numbers[index+2]
    if first < second and first < third:
        strings += " " + str(first)
    elif second < third:
        strings += " " + str(second)
    else:
        strings += " " + str(third)
    index += 3

print("strings")
print(strings)