from FileOperator import FileOperator

numbers = FileOperator("data/data9.txt").change_to_float()

print(numbers)


def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    return bmi_value


def bmi_grade(data):
    grades = ""
    index = 1
    for i in range(0, int(data[0])):
        bmi_value = bmi(data[index], data[index+1])
        if bmi_value < 18.5:
            grades += "under "
        elif bmi_value < 25.0:
            grades += "normal "
        elif bmi_value < 30.0:
            grades += "over "
        else:
            grades += "obese "
        index += 2
    return grades

print(bmi_grade(numbers))

