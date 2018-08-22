from FileOperator import FileOperator
numbers = FileOperator("data10.txt").change_to_integer()

def sum_of(data):
    index = 1
    all_sums = ""
    for i in range(0, data[0]):
        first = data[index]
        step = data[index+1]
        n_step = data[index+2]
        sum = int(((first+(first+(step*(n_step-1))))/2)*n_step)
        all_sums += " " + str(sum)
        index += 3
    return all_sums


print(sum_of(numbers))