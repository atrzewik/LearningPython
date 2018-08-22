from FileOperator import FileOperator
numbers = FileOperator("data13.txt").change_to_float()

def roliing(data):
    result = ""
    for i in range(0, int(data[0])):
        multiply = data[i+1] * 6
        multiply = int(multiply)
        multiply += 1
        result += " " + str(multiply)
    return result


print(roliing(numbers))
