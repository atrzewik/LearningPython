from FileOperator import FileOperator
numbers = FileOperator("data2.txt").change_to_integer()
print(numbers)
print("minimum 1")
indexio = 1
for i in range (0, numbers[0]):
    print(min(numbers[indexio], numbers[indexio+1], numbers[indexio+2]), end= " ")
    indexio += 3

print("\nminimum 2")
index = 1
for i in range(0, numbers[0]):
    #print("index value: ")
    #print(index)
    if numbers[index] < numbers[index+1]:
        if numbers[index] < numbers[index+2]:
            print(numbers[index], end=" ")
    elif numbers[index+1] < numbers[index+2]:
        print(numbers[index+1], end=" ")
    else:
        print(numbers[index+2], end=" ")
    index += 3
