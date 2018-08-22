from FileOperator import FileOperator
numbers = FileOperator("data11.txt").change_to_integer()

def triangle_or_not(data):
    index = 1
    answer = ""
    for i in range(0, data[0]):
        triangle = data[index:index+3]
        triangle = sorted(triangle)
        first_side = triangle[0]
        second_side = triangle[1]
        third_side = triangle[2]
        if first_side + second_side >= third_side:
            answer += " 1"
        else:
            answer += " 0"
        index += 3
    return answer


print(triangle_or_not(numbers))