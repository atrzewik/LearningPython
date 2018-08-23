from FileOperator import FileOperator

numbers = FileOperator("data/data22.txt").change_to_integer()

from math import ceil

def Tryer(datas):
    zero = datas[0]
    data = datas[1:]
    index = 0
    result = ""
    for i in range(0, zero):
        x = data[index]
        y = data[index+1]
        n = data[index+2]
        time = min((ceil((max((x,y)) / float(x+y)) * n) * min((x,y)),
     ceil((min((x,y)) / float(x+y)) * n) * max((x,y))))
        time = str(time)
        result += " " + time
        index += 3
    return result


print(Tryer(numbers))
