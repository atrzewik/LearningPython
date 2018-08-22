from FileOperator import FileOperator
numbers = FileOperator("data/data21.txt").change_to_integer()


def how_many(data):
    one = data[1]
    all = data[2:]
    result = ""
    for i in range(0, one):
        sums = 0
        for n in all:
            if i + 1 == n:
                sums += 1
        result += " " + str(sums)
    return result


print(how_many(numbers))
